from odoo import models,fields

class TravelItinerary(models.Model):
    _inherit="product.product"


    day = fields.Integer(string='Day Number', required=True)
    description = fields.Text(string='Description')
    location = fields.Char(string='Location', required=True)