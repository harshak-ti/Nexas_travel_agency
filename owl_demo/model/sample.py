from odoo import fields,models

class Sample(models.Model):
    _name="sample"
    

    name=fields.Char(string="Name")