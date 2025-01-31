# -*- coding: utf-8 -*-
# from odoo import http


# class IgbBarrasaSystem(http.Controller):
#     @http.route('/igb_barrasa_system/igb_barrasa_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/igb_barrasa_system/igb_barrasa_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('igb_barrasa_system.listing', {
#             'root': '/igb_barrasa_system/igb_barrasa_system',
#             'objects': http.request.env['igb_barrasa_system.igb_barrasa_system'].search([]),
#         })

#     @http.route('/igb_barrasa_system/igb_barrasa_system/objects/<model("igb_barrasa_system.igb_barrasa_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('igb_barrasa_system.object', {
#             'object': obj
#         })

