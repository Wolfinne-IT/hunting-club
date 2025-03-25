from odoo import models, fields


class ModelGun(models.Model):
    _name = 'hunting_club.model_gun'
    _description = 'Model Gun'

    title = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)
