from odoo import models, fields

class FBIAlerta(models.TransientModel):
    _name = 'igb_darkweb.fbi_alerta'
    _description = 'Alerta del FBI'

    mensaje = fields.Text(default="Te hemos pillado intentando comprar, somos el FBI, estás detenido.")

    def cerrar(self):
        return {'type': 'ir.actions.act_window_close'}
