from odoo import models,fields,api

class Choices(models.Model):
    _name="choice"
    _description="Enter choice"

    name=fields.Char(string="Enter Choice")