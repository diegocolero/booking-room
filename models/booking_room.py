from odoo import models, fields

class BookingRoom(models.Model):
    _name = "booking.room"

    name = fields.Char("Nombre", required=True )
