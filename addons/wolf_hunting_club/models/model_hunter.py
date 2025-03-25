from odoo import models, fields


class ModelHunter(models.Model):
    _name = 'hunting_club.model_hunter'
    _description = 'Model Hunter'

    # Basic personal info
    name = fields.Char(string="Ime i Prezime", required=True)
    jmb = fields.Char(string="JMB")  # Jedinstveni Matični Broj
    birth_year = fields.Integer(string="Godina rođenja")
    place_of_residence = fields.Char(string="Mjesto stanovanja")
    address = fields.Char(string="Adresa stanovanja")
    id_card_number = fields.Char(string="Broj lične karte")

    # Hunter membership info
    hunter_course_date = fields.Date(string="Datum polaganja lovačke obuke")
    certificate_number = fields.Char(string="Broj uvjerenja")
    membership_card_number = fields.Char(string="Broj članske knjižice")
    membership_date = fields.Date(string="Datum upisa")

    # Weapon info (example with 2 or 3 weapons)
    weapon1_make = fields.Char(string="Marka 1")
    weapon1_caliber = fields.Char(string="Kalibar 1")
    weapon1_serial = fields.Char(string="Serijski broj 1")

    weapon2_make = fields.Char(string="Marka 2")
    weapon2_caliber = fields.Char(string="Kalibar 2")
    weapon2_serial = fields.Char(string="Serijski broj 2")

    # Optionally add a 3rd if needed
    weapon3_make = fields.Char(string="Marka 3")
    weapon3_caliber = fields.Char(string="Kalibar 3")
    weapon3_serial = fields.Char(string="Serijski broj 3")

    # Additional fields
    # e.g., pol, datum rođenja, etc., if the form requires
    # gender = fields.Selection([('m', 'Muški'), ('f', 'Ženski')], string="Pol")
    # birth_date = fields.Date(string="Datum rođenja")
