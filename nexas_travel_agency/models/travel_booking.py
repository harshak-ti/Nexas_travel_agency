from odoo import fields,models,api

class TravelBooking(models.Model):
    _name='travel.booking'
    _description='Travel Booking'
    _rec_name="reference"
    _inherit=['mail.thread']


    reference=fields.Char(string='Booking Reference',default='New')
    trip_id = fields.Many2one('travel.trip', string='Trip', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    booking_date = fields.Datetime(string='Booking Date', default=fields.Datetime.now)
    status = fields.Selection([
        
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='pending',tracking=True)
    payment_id = fields.Many2one('account.payment', string='Payment')


    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            if not val.get('reference') or val['reference']=='New':
                val['reference']=self.env['ir.sequence'].next_by_code('travel.booking')
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            self.status='confirmed'
    
    def action_cancel(self):
        for rec in self:
            self.status='cancelled'
