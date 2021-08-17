from odoo import api,fields,models


class SchoolNew(models.Model):
    _name = 'school.new'


    name = fields.Char(string='Name')
    roll_no=fields.Integer(string='Roll No')
    division=fields.Char('Div')






