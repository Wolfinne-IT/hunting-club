from odoo import models, fields


class ModelGun(models.Model):
    _name = 'my_module.model_gun'
    _description = 'Model Gun'

    title = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)
