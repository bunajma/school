from odoo import fields, models, api


class Class(models.Model):
    _name = 'school.class'
    _description = 'This is class table'

    code = fields.Char('Code')
    max_students = fields.Integer('Max Students Allowed')
    is_full = fields.Boolean('Is Full', default=False)


