# -*- coding: utf-8 -*-
{
    'name': "Sales Campaigns",
    'summary': """Sales Campaigns""",
    'description': """Sales Campaigns""",
    'website': "",
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'sale', 'crm', 'mass_mailing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_campaign_view.xml',
        'views/sales_campaign_view.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
