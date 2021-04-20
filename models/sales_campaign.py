# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalesCampaign(models.Model):
    _inherit = 'utm.campaign'

    active = fields.Boolean(
        string='Active',
        default=True,
        required=True)
