from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

  
    preferences = fields.Text(string='Preferences')
    sample=fields.Text(string="sample")


    def _send_order_confirmation_mail(self):
        email_template=self.env.ref('nexas_travel_agency.mail_template_sale_confirmation_new')
        email_template.send_mail(self.id,force_send=True)
        

    