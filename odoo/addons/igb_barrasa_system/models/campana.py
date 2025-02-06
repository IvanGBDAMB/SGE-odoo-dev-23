from odoo import models, fields
import random

class Campana(models.Model):
    _name = 'igb_barrasa_system.campana_espia'
    _description = 'Campaña de espia web'

    nombre = fields.Char(string='Nombre', required=True)
    imagen = fields.Binary(string='Imagen')
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today)