from odoo import models,fields,api
import logging
_l=logging.getLogger(__name__)

class TravelTrip(models.Model):
    _inherit=['product.product']


   
    start_date=fields.Date(string='Start Date')
    end_date=fields.Date(string='End Date')
    destination=fields.Char(string='Destination')
    can_trip=fields.Boolean(string="Agency Down",compute="_compute_agency_down",precompute=True)

    trip_type = fields.Selection([
        ('business', 'Business Trip'),
        ('leisure', 'Leisure Trip'),
        ('adventure', 'Adventure Trip'),
        ('pilgrimage', 'Pilgrimage'),
    ], string="Trip Type", default='leisure')


    def create(self,vals):
        is_agency_down = self.env['ir.config_parameter'].sudo().get_param('travel_agency.is_agency_down')
        
        if is_agency_down:
            raise models.ValidationError("The server is down. You cannot create new trips at the moment.")
        else:
            return super(TravelTrip,self).create(vals)
        
    @api.depends('start_date')
    def _compute_agency_down(self):
        is_agency_down = self.env['ir.config_parameter'].sudo().get_param('travel_agency.is_agency_down')
        _l.info(f"\n Is agency down :{is_agency_down}\n")
        if is_agency_down:
            self.can_trip=bool(is_agency_down)
        else:
            self.can_trip=False
