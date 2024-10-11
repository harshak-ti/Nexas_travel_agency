# todo_list/models/todo.py

from odoo import models, fields

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(string='Task', required=True)
    done = fields.Boolean(string='Done', default=False)
    priority = fields.Integer(string='Priority')
    action = fields.Selection([
        ('create', 'Create a new customer'),
        ('exist', 'Link to an existing customer'),
        ('nothing', 'Do not link to a customer')
    ], string='Related Customer')

    stage_id=fields.Many2one('owl.stage',String="Stage")



    