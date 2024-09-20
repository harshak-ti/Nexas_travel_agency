from odoo import fields,models

class ResCompany(models.Model):
    _inherit="res.company"
    _check_company_auto = True

    is_agency_down = fields.Boolean(
        string='Agency Down',
        help="Check this box to mark the agency as down for this company."
    )
    is_booking_allowed = fields.Boolean(
        string='Allow Booking',
        help="Enable or disable bookings for this company."
    )
    is_itinerary_allowed = fields.Boolean(
        string='Allow Itinerary',
        help="Enable or disable itinerary creation for this company."
    )