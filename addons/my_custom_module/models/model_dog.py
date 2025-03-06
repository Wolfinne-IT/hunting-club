from odoo import models, fields


class ModelDog(models.Model):
    _name = 'my_module.model_dog'
    _description = 'Model Dog'

    code = fields.Char(string="Code", required=True)
    value = fields.Float(string="Value")
