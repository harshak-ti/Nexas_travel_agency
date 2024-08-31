from odoo import fields,models

class TravelAgency(models.Model):
    _name="travel.agency"
    _description="Travel Agency Details"


    name=fields.Char(string="Agency Name",size=6,translate=True,required=True,trim=True)
    date_of_opening=fields.Date(string="Opening Date",required=True)
    opening_time=fields.Datetime(string="Opening Time Daily",required=True)
    closing_time=fields.Datetime(string="Closing Time Daily",required=True)
    description=fields.Text(string="Description")
    net_worth=fields.Float(string="Net Worth",digits=(6,2))
    total_employess=fields.Integer(string="Total Employees")
    verified=fields.Boolean(string="Verfied")
    document=fields.Binary(string="Documents",attachment=True)
    description_html=fields.Html(string="HTML",sanitize=True)
    owner_image=fields.Image(string="Image",max_width=1024,max_height=768,verify_resolution=True)
    currency_id=fields.Many2one('res.currency',string='Currency')
    tax_amount=fields.Monetary(string="Tax Amount",currency_field="currency_id")
    agency_type=fields.Selection([('start_up','StartUp'),('enterprise','Enterprise')],string="Agency Type")