from odoo import models, fields


class ModelHunter(models.Model):
    _name = 'my_module.model_hunter'
    _description = 'Model Hunter'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    address = fields.Char(string="Address")
    date_of_birth = fields.Date(string="Date of Birth")
    job = fields.Char(string="Job")
    id_number = fields.Char(string="ID Number")
