# -*- coding: utf-8 -*-

{
    "name": 'report_ng',
    "description": u"""Add commun report action / setup""",
    "version": "0.1",
    "depends": [
        'base',
        'report',
    ],
    "author": "None",
    "category": "Tools",
    "installable": True,
    "data": [
        'views/ir_ui_view_view.xml',
        'views/report_style_layout.xml',
        'views/layout_header_view.xml',
        'views/layout_footer_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_templates_view.xml',
        'data/ir_rule.xml',
    ],
}
