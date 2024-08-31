from odoo import models, fields

class TravelReport(models.Model):
    _name = 'travel.report'
    _description = 'Travel Report'

    report_type = fields.Selection([
        ('sales', 'Sales'),
        ('customer', 'Customer'),
        ('supplier', 'Supplier')
    ], string='Report Type', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    data = fields.Binary(string='Report Data')