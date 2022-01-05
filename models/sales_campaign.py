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
    opportunities_count = fields.Integer(
        string="Lead counts",
        requered=False
    )
    question = fields.Many2many(
        'campaign.questions',
        string="Questions",
        required=False
    )


class CampaignsQuestions(models.Model):
    _name = 'campaign.questions'
    _description = 'Campaign Questions'

    name = fields.Char(
        string="Your questions",
        required=False
    )
    answers = fields.Char(
        string="Your answers",
        required=False,
    )


class CampaignsAnswers(models.Model):
    _name = 'campaign.answers'
    _description = 'Campaign Answers'
#
#     answer = fields.Char(
#         string="Answer",
#         required=False
#     )
#     name = fields.Many2many(
#         'campaign.questions',
#         string="Questions",
#         required=False
#     )
