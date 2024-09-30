from odoo import fields,models,api
import base64
import logging

_l=logging.getLogger(__name__)
class TravelBooking(models.Model):
    _name='travel.booking'
    _description='Travel Booking'
    _rec_name="reference"
    _inherit=['mail.thread']


    reference=fields.Char(string='Booking Reference',default='New')
    trip_id = fields.Many2one('travel.trip', string='Trip', required=True,ondelete='cascade')
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    booking_date = fields.Datetime(string='Booking Date', default=fields.Datetime.now)
    status = fields.Selection([
        
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='pending',tracking=True)
    payment_id = fields.Many2one('account.payment', string='Payment')
    trip_ids=fields.Many2many('travel.trip','trip_booking_rel','trip_id','name',string='Trips',ondelete='cascade')


    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            if not val.get('reference') or val['reference']=='New':
                val['reference']=self.env['ir.sequence'].next_by_code('travel.booking')
        if 'trip_id' in val and not val['trip_id']:
            raise ValueError("The trip_id must be provided and valid.")
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            self.status='confirmed'
    
    def action_cancel(self):
        for rec in self:
            self.status='cancelled'

    def confirm_booking(self):
        self.ensure_one()
        self.status = 'confirmed'
        return True
    

    def send_booking_mail(self):
        email_template=self.env.ref('nexas_travel_agency.email_template_travel_booking')
        email_template.send_mail(self.id,force_send=True)


    def send_email_with_pdf_report(self):

    # Generate the PDF report
        pdf_report = self.env['ir.actions.report'].sudo()._render_qweb_pdf('nexas_travel_agency.report_travel_booking', [self.id])[0]
        _l.info(f"PDF Report --------------> {pdf_report}\n")

        # Encode the PDF to base64
        encoded_pdf = base64.b64encode(pdf_report)
        _l.info(f"Encoded PDF Report --------------> {pdf_report}\n")


        # Create the email with the necessary values
        email_values = {
            'subject': 'Test Email with PDF Report Attachment',
            'email_from': self.env.company.email,  # Get the current company email
            'email_to': self.customer_id.email,  # Send to the customer email
            'body_html': '<p>Hello,</p><p>This is a test email with a PDF report attachment.</p>',
            'auto_delete': True,  # Automatically delete the email after sending
            'attachment_ids': [(0, 0, {  # Attach the PDF directly while creating the email
                'name': 'ReportAttachment.pdf',
                'type': 'binary',
                'datas': encoded_pdf.decode('utf-8'),
                'res_model': 'mail.mail',
                'res_id': 0,
                'mimetype': 'application/pdf'  # Set the correct MIME type
            })]
        }
        _l.info(f"Decoded PDF Report --------------> {encoded_pdf.decode('utf-8')}\n")


        # Create the mail.mail record
        mail = self.env['mail.mail'].create(email_values)

        # Send the email
        mail.send()

        return True


