# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmCampaign(models.Model):
    _inherit = 'crm.lead'

    sales_campaign_id = fields.Many2one(
        'sales_campaigns.campaign',
        string='Sales Campaign',
        help='Sales campaign name.',
        required=False
    )
    questions = fields.Many2many(
        'campaign.answers',
        string="Questions",
        required=False
    )

    @api.onchange('sales_campaign_id')
    def _onchange_sales_campaign(self):
        self.questions = self.sales_campaign_id.campaign_questions

