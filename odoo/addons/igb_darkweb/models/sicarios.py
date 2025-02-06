from odoo import models, fields

class Sicario(models.Model):
    _name = 'igb_darkweb.sicario'
    _description = 'Sicarios Disponibles'

    nombre = fields.Char(string='Nombre', required=True)
    tarifa = fields.Float(string='Tarifa', required=True)
    especialidad_ids = fields.Many2many('igb_darkweb.arma', string='Especialidades')

    def abrir_alerta_fbi(self):
        """Abre el wizard con la alerta del FBI"""
        return {
            'name': 'FBI Alert',
            'type': 'ir.actions.act_window',
            'res_model': 'igb_darkweb.fbi_alerta',
            'view_mode': 'form',
            'target': 'new',
        }
