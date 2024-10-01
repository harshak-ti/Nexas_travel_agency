# todo_list/models/todo.py

from odoo import models, fields

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(string='Task', required=True)
    done = fields.Boolean(string='Done', default=False)
