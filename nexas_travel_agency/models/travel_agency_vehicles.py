from odoo import models, fields,api

class TravelAgencyVehicle(models.Model):
    _name = 'travel.agency.vehicles'
    _description = 'Vehicle Details'

    _order='capacity'
   

    name = fields.Char(string='Vehicle Name', required=True)
    license_plate = fields.Char(string='License Plate', required=True)
    model = fields.Char(string='Model')
    manufacturer = fields.Char(string='Manufacturer')
    year_of_manufacture = fields.Integer(string='Year of Manufacture')
    vehicle_type = fields.Selection([
        ('car', 'Car'),
        ('bus', 'Bus'),
        ('motorcycle', 'Motorcycle'),
        ('van', 'Van')
    ], string='Vehicle Type')
    capacity=fields.Integer(string="Number of seats",compute="_compute_num_of_seats",readonly=False,store=True)
    color = fields.Char(string='Color')
 
    status = fields.Selection([
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'In Maintenance'),
        ('retired', 'Retired')
    ], string='Status', default='available')
 
    driver_id = fields.Many2one('travel.agency.drivers', string='Assigned Driver')

    @api.depends('vehicle_type')
    def _compute_num_of_seats(self):
        for rec in self:
            if rec.vehicle_type :
                if rec.vehicle_type=='car':
                    rec.capacity=4
                elif rec.vehicle_type=='bus':
                    rec.capacity=50
                elif rec.vehicle_type=='motorcycle':
                    rec.capacity=1
                else:
                    rec.capacity=20


    def write(self,vals):
        res=super(TravelAgencyVehicle,self).write(vals)
        if 'driver_id' in vals:
            for rec in self:
                rec.driver_id.vehicle_id=rec.id
        return res
    
    def create(self,vals):
        res=super(TravelAgencyVehicle,self).create(vals)
        if res.driver_id:
            res.driver_id.vehicle_id=res.id
        return res
            



