from odoo import models, fields,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    travel_history_ids = fields.One2many('travel.booking', 'customer_id', string='Travel History',readonly=True)
    preferences = fields.Text(string='Travel Preferences')


    def custom_create_btn(self):
        self.ensure_one()
        self.write(self._convert_to_write(self.read()[0]))
        return True
    
    @api.model
    def create(self,vals):
        res=super(ResPartner,self).create(vals)
        res.preferences="Manali,jaipur"
        return res
    

    def action_preview_sale_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }
