from odoo import models, fields

class TravelProduct(models.Model):
    _name = 'travel.product'
    _description = 'Travel Product'
    _rec_name="trip_id"
    _inherit=['mail.thread']


   
    trip_id = fields.Many2one('travel.trip', string='Trip',required="True")
    product_id=fields.Many2one('product.product',string="Products")
    qty=fields.Float(string="Quantity")

