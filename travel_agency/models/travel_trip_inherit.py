from odoo import models,fields,api


class TravelTrip(models.Model):
    _inherit=['product.product']


   
    start_date=fields.Date(string='Start Date')
    end_date=fields.Date(string='End Date')
    destination=fields.Char(string='Destination')

    trip_type = fields.Selection([
        ('business', 'Business Trip'),
        ('leisure', 'Leisure Trip'),
        ('adventure', 'Adventure Trip'),
        ('pilgrimage', 'Pilgrimage'),
    ], string="Trip Type", default='leisure')


    def create(self,vals):
        is_agency_down = self.env['ir.config_parameter'].sudo().get_param('travel_agency.is_agency_down')
        
        if is_agency_down:
            raise models.ValidationError("The agency is down. You cannot create new trips at the moment.")
        else:
            return super(TravelTrip,self).create(vals)