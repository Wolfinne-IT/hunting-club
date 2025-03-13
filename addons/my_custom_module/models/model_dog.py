from odoo import models, fields


class ModelDog(models.Model):
    _name = 'my_module.model_dog'
    _description = 'Model Dog'

    # Basic info
    name = fields.Char(string="Ime psa", required=True)  # dog's name
    breed = fields.Char(string="Rasa")
    sex = fields.Selection([
        ('m', 'Muški'),
        ('f', 'Ženski')
    ], string="Pol")
    birth_date = fields.Date(string="Datum rođenja")

    # Contact / location
    phone = fields.Char(string="Telefon")
    place_of_residence = fields.Char(string="Mjesto stanovanja")
    address = fields.Char(string="Ulica")

    # Registration / membership info
    registration_number = fields.Char(string="Reg. broj")
    date_issued = fields.Date(string="Datum izdavanja")
    membership_date = fields.Date(string="Datum upisa u knjigu")

    # Exhibition rating / notes
    expo_rating = fields.Char(string="Ocjena na izložbama")

    # Parent info
    father_name = fields.Char(string="Ime oca")
    mother_name = fields.Char(string="Ime majke")

    # Link to owner (optional if you want to connect to Hunter)
    owner_id = fields.Many2one('my_module.model_hunter', string="Vlasnik")
