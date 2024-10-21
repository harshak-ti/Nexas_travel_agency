from odoo import models,api
from odoo.tools import float_compare, float_round
from odoo.exceptions import  ValidationError

class StockMove(models.Model):
    _inherit = 'stock.move'


    @api.onchange('quantity')
    def validate_quantity(self):
        self.ensure_one()
        if self.picking_type_id and not self.picking_type_id.use_extra_quantity:
            rounding = self.env['decimal.precision'].precision_get('Product Unit of Measure')
            quantity_in_demand_uom = self.product_uom._compute_quantity(self.quantity, self.product_id.uom_id, rounding_method='HALF-UP')
            quantity_in_demand_uom = float_round(quantity_in_demand_uom, precision_digits=rounding)
            product_uom_qty_converted = self.product_id.uom_id._compute_quantity(self.product_uom_qty, self.product_uom, rounding_method='HALF-UP')
            if float_compare(quantity_in_demand_uom, product_uom_qty_converted, precision_digits=rounding) > 0:
                raise ValidationError("The quantity cannot be greater than the demand.")
        return



       