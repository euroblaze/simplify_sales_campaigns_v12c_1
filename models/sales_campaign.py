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
        requered=False,
        compute="_crm_opportunities_count"
    )
    all_campaign_questions = fields.Many2many(
        'campaign.questions',
        string="Questions",
        required=False
    )
    campaign_questions = fields.One2many(
        'campaign.answers',
        'campaign_question',
        string="Answers",
        required=False)

    @api.constrains("all_campaign_questions")
    def number_of_campaign_questions(self):
        for record in self:
            campaign_questions = record.env["campaign.answers"].search([('campaign_question', '=', record.id)])
            for i in range(0, len(campaign_questions)):
                flag = False
                for j in range(0, len(record.all_campaign_questions)):
                    if campaign_questions[i].question.id == record.all_campaign_questions[j].id:
                        flag = True
                        break

                if not flag:
                    campaign_questions[i].unlink()

            for i in range(0, len(record.all_campaign_questions)):
                obj = record.env["campaign.answers"].search([
                    ('campaign_question', '=', record.id),
                    ('question', '=', record.all_campaign_questions[i].id)
                ])

                if not obj:
                    record.env["campaign.answers"].create({
                        'campaign_question': record.id,
                        'question': record.all_campaign_questions[i].id
                    })

    def _crm_opportunities_count(self):
        for record in self:
            opportunities = record.env['crm.lead'].search([('sales_campaign_id', '=', record.id)])
            record.opportunities_count = len(opportunities)


class CampaignsQuestions(models.Model):
    _name = 'campaign.questions'
    _description = 'Campaign Questions'

    name = fields.Char(
        string="Questions",
        required=False
    )
    question_answer = fields.One2many(
        'campaign.answers',
        'question',
        string="Answers",
        required=False,
        readonly=True)

    answer_type = fields.Selection([
        ('yes_no', 'Yes/No'),
        ('short_answer', 'One line answer'),
        ('long_answer', 'Up to 200 characters answer')
    ], requered=True, default='short_answer')


class CampaignsAnswers(models.Model):
    _name = 'campaign.answers'
    _description = 'Campaign Answers'

    answer_type = fields.Selection(related='question.answer_type')
    answer1 = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Yes/No')
    answer2 = fields.Char(string="Your short answer", required=False)
    answer3 = fields.Text(string="Your long answer", required=False)
    question = fields.Many2one(
        'campaign.questions',
        string="Questions",
        required=False,
        readonly=True)
    campaign_question = fields.Many2one(
        'sales_campaigns.campaign',
        string="Course",
        required=False,
        readonly=True)
