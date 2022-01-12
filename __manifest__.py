# -*- coding: utf-8 -*-
{
    'name': "Sales Campaigns",
    'summary': """Sales Campaigns""",
    'description': """Sales Campaigns""",
    'author': "Bojan Anchev and Bojan Dimoski",
    'website': "m102@simplify-erp.com, m114@simplify-erp.com",
    'category': 'Productivity',
    'version': '0.1',

    'depends': ['base', 'sale', 'sale_management', 'crm'],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_campaign_view.xml',
        'views/sales_campaign_view.xml',
        'views/questions.xml',
        'views/views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
