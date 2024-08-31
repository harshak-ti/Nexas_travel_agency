from odoo import fields,models,api

class TravelTrip(models.Model):
    _name='travel.trip'
    _description='Travel Trip'
    _rec_name="reference"
    _inherit=['mail.thread']



    reference=fields.Char(string='Trip Reference',default='New')
    name=fields.Char(string='Trip Name',required=True)
    start_date=fields.Date(string='Start Date',required=True)
    end_date=fields.Date(string='End Date',required=True)
    destination=fields.Char(string='Destination',required=True)
    booking_ids=fields.One2many(comodel_name='travel.booking',inverse_name='trip_id',string='Bookings')
    itinerary_ids=fields.One2many(comodel_name='travel.itinerary',inverse_name='trip_id',string="Itineraries")
    products_ids=fields.One2many(comodel_name='travel.product',inverse_name='trip_id',string="Products")
    total_qty=fields.Float(compute="_compute_total_qty",string="Total Quantity")

    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            if not val.get('reference') or val['reference']=='New':
                val['reference']=self.env['ir.sequence'].next_by_code('travel.trip')
        return super().create(vals_list)
    

    @api.depends('reference')
    def _compute_display_name(self):
        for trip in self:
            trip.display_name = f"[{trip.reference}] {trip.name}"

    
    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty=sum(rec.products_ids.mapped('qty'))
        


    
    


    
