{
    'name': 'report_ng',
    'version': '0.1',
    'category': 'Tools',
    'summary': 'Next generation report utils',
    'description': """Add commun report action / setup""",
    'depends': ['base', 'report'],
    'data': [
        'views/report_style_layout.xml',
        'views/ir_ui_view_view.xml',
        'views/layout_header_view.xml',
        'views/layout_footer_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_templates_view.xml',
    ],
    'installable': True,
    'application': False,
}
