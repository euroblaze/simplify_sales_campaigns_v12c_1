# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmCampaign(models.Model):
    _inherit = 'crm.lead'

    campaign_id = fields.Many2one(
        'utm.campaign',
        string='Campaign',
        help='Sales Campaign',
        required=False)
