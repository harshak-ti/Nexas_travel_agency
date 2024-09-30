from odoo import models,fields


class Website(models.Model):
    _inherit='website'


    is_website_allowed=fields.Boolean(string="Allow Website")