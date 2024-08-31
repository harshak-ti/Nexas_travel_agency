from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    booking_id = fields.Many2one('travel.booking', string='Booking')