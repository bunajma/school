from odoo import fields, models, api


class Subject(models.Model):
    _name = 'school.subject'
    _description = 'School Subjects'

    name = fields.Char(string='Title')
    #101
    code = fields.Char(string='Code')
    level = fields.Selection([
        ('0', 'Primary'),
        ('1', 'Middle'),
        ('2', 'Advance')
    ], string='Level')
    active = fields.Boolean('Active')
    credit = fields.Integer(string='Credit')




