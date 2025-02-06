from odoo import models, fields

class Arma(models.Model):
    _name = 'igb_darkweb.arma'
    _description = 'Armas Disponibles'

    nombre = fields.Char(string='Nombre', required=True)
    precio = fields.Float(string='Precio', required=True)
    distribuidor_id = fields.Many2one('res.partner', string='Distribuidor')

    def abrir_alerta_fbi(self):
        """Abre el wizard con la alerta del FBI"""
        return {
            'name': 'FBI Alert',
            'type': 'ir.actions.act_window',
            'res_model': 'igb_darkweb.fbi_alerta',
            'view_mode': 'form',
            'target': 'new',
        }
