from odoo import models, fields,api

class TravelItinerary(models.Model):
    _name = 'travel.itinerary'
    _description = 'Travel Itinerary'
    _rec_name="trip_id"
    _inherit=['mail.thread']


    reference=fields.Char(string='Itinerary Reference',default='New')
    trip_id = fields.Many2one('travel.trip', string='Trip', required=True,ondelete='cascade')
    day = fields.Integer(string='Day Number', required=True)
    description = fields.Text(string='Description')
    location = fields.Char(string='Location', required=True)


    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            if not val.get('reference') or val['reference']=='New':
                val['reference']=self.env['ir.sequence'].next_by_code('travel.itinerary')
        return super().create(vals_list)