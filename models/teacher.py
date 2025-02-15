from odoo import fields, models, api


class Teacher(models.Model):
    # _name = 'school.teacher'
    _inherit = 'hr.employee'
    _description = 'Add teaching related data'

    office_hours = fields.Text('Office Hours')
    cert = fields.Binary(string='Certificate')

