from odoo import models, fields, api
from ast import literal_eval

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    user_ids = fields.Many2many('res.users', string="Accessible Users", 
                                help="Users who can access this operation type.")
    

    def _get_action(self, action_xmlid):

        action = self.env["ir.actions.actions"]._for_xml_id(action_xmlid)
        if self:
            action['display_name'] = self.display_name

        action['domain'] = [('picking_type_id', '=', self.id)]
        return action

   