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