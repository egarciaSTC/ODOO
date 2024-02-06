import string
from odoo import models, fields, api

class PruebaOdoo(models.Model):
    _name = "service.detail"
    _description = "Modulo para guardar el detalle de los servicios"

    servicio_detalle = fields.Text(String="Detalle del Servicio")
    cliente = fields.Many2one('res.partner', string="Cliente")
    servicio = fields.Many2one('product.template', string="Servicio", domain="[('detailed_type', 'ilike', 'serv')]")