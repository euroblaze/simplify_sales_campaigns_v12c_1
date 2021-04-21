# -*- coding: utf-8 -*-
{
    'name': "Sales Campaigns",
    'summary': """Sales Campaigns""",
    'description': """Sales Campaigns""",
    'website': "",
    'category': 'Productivity',
    'version': '0.1',

    'depends': ['base', 'sale', 'sale_management', 'crm'],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_campaign_view.xml',
        'views/sales_campaign_view.xml',
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
