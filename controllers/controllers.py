# -*- coding: utf-8 -*-
from odoo import http

# class Salescampaign(http.Controller):
#     @http.route('/salescampaign/salescampaign/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salescampaign/salescampaign/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('salescampaign.listing', {
#             'root': '/salescampaign/salescampaign',
#             'objects': http.request.env['salescampaign.salescampaign'].search([]),
#         })

#     @http.route('/salescampaign/salescampaign/objects/<model("salescampaign.salescampaign"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salescampaign.object', {
#             'object': obj
#         })