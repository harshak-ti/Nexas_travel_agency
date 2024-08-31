from odoo import models, fields

class TravelSupplier(models.Model):
    _name = 'travel.supplier'
    _description = 'Travel Supplier'

    name = fields.Char(string='Supplier Name', required=True)
    contact_info = fields.Text(string='Contact Information')
    services_provided = fields.Text(string='Services Provided')