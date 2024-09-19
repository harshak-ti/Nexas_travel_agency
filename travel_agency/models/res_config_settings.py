from odoo import models,fields


class ReportConfigSettings(models.TransientModel):
   
    _inherit = ["res.config.settings"]


    is_agency_down=fields.Boolean(string="Agency Down", config_parameter='travel_agency.is_agency_down')
    
