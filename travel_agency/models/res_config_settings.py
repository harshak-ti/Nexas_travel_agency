from odoo import models,fields


class ReportConfigSettings(models.TransientModel):
   
    _inherit = "res.config.settings"

    def _default_website(self):
        return self.env['website'].search([('company_id', '=', self.env.company.id)], limit=1)

    website_id = fields.Many2one(
        'website',
        string="website",
        default=_default_website, ondelete='cascade')
    
    is_agency_down=fields.Boolean(related='company_id.is_agency_down',string="Agency Down",readonly=False)

    is_booking_allowed=fields.Boolean(related='company_id.is_booking_allowed',string="Allow Booking",readonly=False)

    is_itinerary_allowed=fields.Boolean(related='company_id.is_itinerary_allowed',string="Allow Itinerary",readonly=False)

    is_website_allowed=fields.Boolean(related='website_id.is_website_allowed',string="Allow Website",readonly=False)
    




    
