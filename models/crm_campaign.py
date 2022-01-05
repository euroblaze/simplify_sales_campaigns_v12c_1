# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmCampaign(models.Model):
    _inherit = 'crm.lead'

    sales_campaign_id = fields.Many2one(
        'sales_campaigns.campaign',
        string='Sales Campaign',
        help='Sales campaign name.',
        required=False)
    answers = fields.Many2many(
        'campaign.questions',
        string="Your questions",
        required=False
    )
