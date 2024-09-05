from odoo import fields,models,api
import logging
_l = logging.getLogger(__name__)


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
    booking_ids=fields.One2many(comodel_name='travel.booking',inverse_name='trip_id',string='Bookings',ondelete='cascade')
    itinerary_ids=fields.One2many(comodel_name='travel.itinerary',inverse_name='trip_id',string="Itineraries",ondelete='cascade')
    products_ids=fields.One2many(comodel_name='travel.product',inverse_name='trip_id',string="Products",ondelete='cascade')
    total_qty=fields.Float(compute="_compute_total_qty",string="Total Quantity")
    hired_vehicle=fields.Many2one('travel.agency.vehicles',string="Vehicles",compute="_compute_vehicle_hired",required=False,store=True,readonly=False,ondelete='cascade')
    hired_driver=fields.Char(string='Driver ',related='hired_vehicle.driver_id.name',readonly=True)

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


    @api.depends('booking_ids')
    @api.onchange('booking_ids')
    def _compute_vehicle_hired(self):
        for rec in self:
            if not rec.booking_ids:
                rec.hired_vehicle = False
                return
            num_of_bookings = sum(1 for booking in rec.booking_ids if booking.status == 'confirmed')
            available_vehicles = self.env['travel.agency.vehicles'].search([
                ('status', '=', 'available'),
                ('capacity', '>=', num_of_bookings)
            ])
            if rec.hired_vehicle:
                rec.hired_vehicle.status = 'available'
                rec.hired_vehicle.driver_id.status='available'
            if available_vehicles:
                rec.hired_vehicle = available_vehicles[0]
            else:
                rec.hired_vehicle = False


    def write(self, vals):
        res = super(TravelTrip, self).write(vals)
        for rec in self:
            if rec.hired_vehicle:
                rec.hired_vehicle.status = 'in_use'
                rec.hired_vehicle.driver_id.status='occupied'
        return res

    @api.model
    def create(self, vals):
        res = super(TravelTrip, self).create(vals)
        if res.hired_vehicle:
            res.hired_vehicle.status = 'in_use'
            res.hired_vehicle.driver_id.status='occupied'
        return res
    
    def unlink(self):
        for rec in self:
                child_record=self.env['travel.booking'].search([('trip_id','=',rec.id)])
                child_record.unlink()
                child_record2=self.env['travel.itinerary'].search([('trip_id','=',rec.id)])
                child_record2.unlink()
                child_record3=self.env['travel.product'].search([('trip_id','=',rec.id)])
                child_record3.unlink()
        return super(TravelTrip,self).unlink()


    def action_save_record(self):
        self.ensure_one()  
        self.write(self._convert_to_write(self.read()[0]))
        return True 


    def view_record_action(self):
        records=self.search([])
        # records=self.browse(records_ids)
        _l.info(f"Displaying self: {self}")
        for rec in records:
            _l.info(f"Display the record : {rec.name}")
            if rec.name=="Jaipur Trip":
                    _l.info(f"Displaying booking ids : ")
                    
                    rec.write({
                            'booking_ids':[(2,rec.booking_ids[0].id,0)]
                })

        return True  
    
    # def view_record_action(self):
    #     records=self.search([])
    #     # records=self.browse(records_ids)
    #     _l.info(f"Displaying self: {self}")
    #     for rec in records:
    #         _l.info(f"Display the record : {rec.name}")
    #         if rec.name=="Jaipur Trip":
    #                 _l.info(f"Displaying booking ids : ")
    #                 existing_products=self.env['travel.product'].search([]).ids
    #                 rec.write({
    #                         'products_ids':[(4,existing_products[0],0)]
    #             })

    #     return True  
    

    # def view_record_action(self):
    #     records=self.search([])
    #     # records=self.browse(records_ids)
    #     _l.info(f"Displaying self: {self}")
    #     for rec in records:
    #         _l.info(f"Display the record : {rec.name}")
    #         if rec.name=="Jaipur Trip":
    #            for booking in rec.booking_ids:
    #                 _l.info(f"Displaying booking ids : {booking}")
    #                 if booking.customer_id.id==1 :
    #                     rec.write({
    #                         'booking_ids':[(1,booking.id,{
                               
    #                             'status':'confirmed'

    #                         })]
    #             })

    #     return True  


    
    


    
