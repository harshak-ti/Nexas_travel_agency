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
