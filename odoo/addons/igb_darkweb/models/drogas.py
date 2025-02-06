from odoo import models, fields, api

class Droga(models.Model):
    _name = 'igb_darkweb.cocaina'
    _description = 'Drogas Disponibles'

    nombre = fields.Char(string='Nombre', required=True)
    precio = fields.Float(string='Precio', required=True)
    proveedor_ids = fields.Many2many('res.partner', string='Proveedores')

    def abrir_alerta_fbi(self):
        """Abre el wizard con la alerta del FBI"""
        return {
            'name': 'FBI Alert',
            'type': 'ir.actions.act_window',
            'res_model': 'igb_darkweb.fbi_alerta',
            'view_mode': 'form',
            'target': 'new',
        }
