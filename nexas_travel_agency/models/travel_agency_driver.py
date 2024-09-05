from odoo import models, fields

class TravelAgencyDriver(models.Model):
    _name = 'travel.agency.drivers'
    _description = 'Driver Details'



    name = fields.Char(string='Name', required=True)
    driver_license_number = fields.Char(string='Driver License Number', required=True)
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    vehicle_id = fields.Many2one('travel.agency.vehicles', string='Vehicle')
    license_expiry_date = fields.Date(string='License Expiry Date')
    date_of_birth = fields.Date(string='Date of Birth')
    hire_date = fields.Date(string='Hire Date')
    profile_image = fields.Image(string='Profile Image')
    status=fields.Selection([('available','Available'),('occupied','Occupied'),('on_leave','On Leave')],string='Status',default='available')
    
