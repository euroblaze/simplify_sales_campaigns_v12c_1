# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalesCampaign(models.Model):
    _name = 'sales_campaigns.campaign'
    _description = 'Sales Campaigns'

    name = fields.Char(
        string='Campaign Name',
        help='Sales campaign name',
        required=True)
    active = fields.Boolean(
        string='Active',
        default=True,
        required=True)
