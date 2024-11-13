# -*- coding: utf-8 -*-
# from odoo import http


# class Iti(http.Controller):
#     @http.route('/iti/iti', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iti/iti/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('iti.listing', {
#             'root': '/iti/iti',
#             'objects': http.request.env['iti.iti'].search([]),
#         })

#     @http.route('/iti/iti/objects/<model("iti.iti"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iti.object', {
#             'object': obj
#         })

