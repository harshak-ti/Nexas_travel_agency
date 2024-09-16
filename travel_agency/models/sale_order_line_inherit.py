from odoo import models, fields

class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    
    product_id = fields.Many2one('product.product', string="Product", domain="[('product_id.destination', '!=', False)]")
