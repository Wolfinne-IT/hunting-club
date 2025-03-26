from odoo import models, fields


class Hunter(models.Model):
    _inherit = 'res.partner'  # Extend the existing Contacts model
    _description = 'Hunter Partner'

    # Mark this contact as a Hunter
    is_hunter = fields.Boolean(string="Is Hunter", default=True)

    # Hunter-specific fields
    jmb = fields.Char(string="JMB")  # Jedinstveni Matični Broj
    birth_year = fields.Integer(string="Godina rođenja")
    id_card_number = fields.Char(string="Broj lične karte")

    # Hunter membership info
    hunter_course_date = fields.Date(string="Datum polaganja lovačke obuke")
    certificate_number = fields.Char(string="Broj uvjerenja")
    membership_card_number = fields.Char(string="Broj članske knjižice")
    membership_date = fields.Date(string="Datum upisa")

    # Weapon info
    weapon1_make = fields.Char(string="Marka 1")
    weapon1_caliber = fields.Char(string="Kalibar 1")
    weapon1_serial = fields.Char(string="Serijski broj 1")

    weapon2_make = fields.Char(string="Marka 2")
    weapon2_caliber = fields.Char(string="Kalibar 2")
    weapon2_serial = fields.Char(string="Serijski broj 2")

    weapon3_make = fields.Char(string="Marka 3")
    weapon3_caliber = fields.Char(string="Kalibar 3")
    weapon3_serial = fields.Char(string="Serijski broj 3")
