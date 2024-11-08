# -*- coding: utf-8 -*-
{
    'name': "Search by VAT/TIN",

    'summary': """
        Search partner by VAT/TIN""",

    'description': """
        Modification of function _name_search in res_partner to allow minus sign in vat/tin
    """,

    'author': "joonza",
    'website': "https://www.joonza.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}