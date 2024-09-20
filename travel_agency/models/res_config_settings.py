from odoo import models,fields


class ReportConfigSettings(models.TransientModel):
   
    _inherit = "res.config.settings"


    is_agency_down=fields.Boolean(related='company_id.is_agency_down',string="Agency Down",readonly=False)

    is_booking_allowed=fields.Boolean(related='company_id.is_booking_allowed',string="Allow Booking",readonly=False)

    is_itinerary_allowed=fields.Boolean(related='company_id.is_itinerary_allowed',string="Allow Itinerary",readonly=False)




    
