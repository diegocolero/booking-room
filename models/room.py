from odoo import models, fields

class Room(models.Model):
    _name = "room"
    _description = "Aulas y espacios"

    name = fields.Char("Nombre", required=True)
    floor = fields.Char("Planta")

    _sql_constraints = [('name_unique', 'unique(name)', 'Ya existe un aula o espacio con ese nombre !')]
