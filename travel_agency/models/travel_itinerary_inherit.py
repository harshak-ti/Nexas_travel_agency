from odoo import models,fields

class TravelItinerary(models.Model):
    _inherit="product.product"


    day = fields.Integer(string='Day Number', required=True)
    description = fields.Text(string='Description')
    location = fields.Char(string='Location', required=True)



    def create(self,vals):
        settings = self.env['res.config.settings'].search([], limit=1)
        # is_agency_down = self.env['ir.config_parameter'].sudo().get_param('travel_agency.is_agency_down')
        is_itinerary_allow = settings and settings.is_itinerary_allowed
        # is_itinerary_allow = self.env['ir.config_parameter'].sudo().get_param('travel_agency.is_itinerary_allowed')
        
        if not is_itinerary_allow:
            raise models.ValidationError("The server is down. You cannot create new booking at the moment.")
        else:
            return super(TravelItinerary,self).create(vals)
