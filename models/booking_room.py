from odoo import models, fields, api

class BookingRoom(models.Model):
    _name = "booking.room"
    _description = "Reserva de aulas/espacios"

    name = fields.Char("Nombre", related='room.name', required=True)
    date_start = fields.Date("Fecha de Inicio", required=True)
    date_stop = fields.Date("Fecha de fin", required=True)
    room = fields.Many2one("room", string="Aula/espacio", required=True)
    user_id = fields.Many2one('res.users', 'Organizador', default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Creado por', related='user_id.partner_id', readonly=True)