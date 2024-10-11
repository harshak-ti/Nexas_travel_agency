from odoo import fields,models


class Stage(models.Model):

    _name="owl.stage"
    _description="This is owl stage"

    name=fields.Char(string="Stage Name")
    