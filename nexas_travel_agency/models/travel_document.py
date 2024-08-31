from odoo import models, fields

class TravelDocument(models.Model):
    _name = 'travel.document'
    _description = 'Travel Document'

    document_type = fields.Selection([
        ('visa', 'Visa'),
        ('ticket', 'Ticket'),
        ('insurance', 'Insurance')
    ], string='Document Type', required=True)
    issued_date = fields.Datetime(string='Issued Date', default=fields.Datetime.now)
    expiry_date = fields.Datetime(string='Expiry Date')
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)