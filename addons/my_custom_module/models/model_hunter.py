from odoo import models, fields


class ModelHunter(models.Model):
    _name = 'my_module.model_hunter'
    _description = 'Model Hunter'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
