# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random

class Campana(models.Model):
    _name = 'igb_barrasa_system.campana_espia'
    _description = 'Campaña de espia web'

    id_espia = fields.Integer(string='ID Espia', readonly=True, copy=False, index=True, unique=True)
    nombre = fields.Char(string='Nombre', required=True)
    imagen = fields.Binary(string='Imagen')
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today)

    @api.model
    def create(self, vals):
        while True:
            random_id = random.randint(100000, 999999)
            if not self.search([('id_espia', '=', random_id)]):
                break
        vals['id_espia'] = random_id
        return super(Campana, self).create(vals)