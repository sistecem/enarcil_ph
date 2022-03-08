# -*- coding: utf-8 -*-
# from odoo import http


# class EnarcilPh(http.Controller):
#     @http.route('/enarcil_ph/enarcil_ph/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enarcil_ph/enarcil_ph/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('enarcil_ph.listing', {
#             'root': '/enarcil_ph/enarcil_ph',
#             'objects': http.request.env['enarcil_ph.enarcil_ph'].search([]),
#         })

#     @http.route('/enarcil_ph/enarcil_ph/objects/<model("enarcil_ph.enarcil_ph"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enarcil_ph.object', {
#             'object': obj
#         })
