from odoo import models, fields,api
import logging
_l=logging.getLogger(__name__)
class ResPartner(models.Model):
    _inherit = 'res.partner'

    travel_history_ids = fields.One2many('travel.booking', 'customer_id', string='Travel History',readonly=True)
    preferences = fields.Text(string='Travel Preferences')
    previous_company_id=fields.Many2one('res.partner',string="Previous Company",readonly=True)
   


    def custom_create_btn(self):
        self.ensure_one()
        self.write(self._convert_to_write(self.read()[0]))
        return True
    
    @api.model
    def create(self,vals):
        return super(ResPartner,self).create(vals)
    



    def write(self, vals):
        if 'parent_id' in vals:
            for partner in self:
                if partner.parent_id:                   
                    vals['previous_company_id'] = partner.parent_id.id
        return super(ResPartner, self).write(vals)

    def action_preview_sale_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }
   
