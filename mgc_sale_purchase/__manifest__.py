# -*- coding: utf-8 -*-
{
    'name': "Vice-versa Sales/Purchase order",
    'summary': """ Vice-versa Sales/Purchase order """,
    'description': """
        SO to create PO with same order line and PO to SO with same order line
    """,
    'author': "Digital Automations srl",
    'website': "https://digitalautomations.it/",
    'category': 'Uncategorized',
    'version': '14.0.1.0.2',
    'depends': [
        'sale_management', 'purchase',
    ],

    'data': [
        'views/sale_views.xml',
        'views/purchase_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
