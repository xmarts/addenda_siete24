# -*- coding: utf-8 -*-
from odoo import http

# class AddendaSiete24(http.Controller):
#     @http.route('/addenda_siete24/addenda_siete24/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addenda_siete24/addenda_siete24/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addenda_siete24.listing', {
#             'root': '/addenda_siete24/addenda_siete24',
#             'objects': http.request.env['addenda_siete24.addenda_siete24'].search([]),
#         })

#     @http.route('/addenda_siete24/addenda_siete24/objects/<model("addenda_siete24.addenda_siete24"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addenda_siete24.object', {
#             'object': obj
#         })