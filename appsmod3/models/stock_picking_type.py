from odoo import models, fields


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    use_extra_quantity=fields.Boolean(string="Use Extra Quantity",help="Allow/Disallow the extra quantity.",default=True,groups='stock.group_stock_manager')



   