from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # preferences = fields.Text(string='Travel Preferences')
    travel_history_ids = fields.One2many('travel.booking', 'customer_id', string='Travel History')