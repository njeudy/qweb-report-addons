# -*- coding: utf-8 -*-

from openerp import models, fields


class irUiView(models.Model):

    _inherit = 'ir.ui.view'

    view_theme_id = fields.Many2one('ir.ui.view.theme', string="Theme")
    company_ids = fields.Many2many('res.company', 'res_company_ir_ui_view_rel', 'user_id', 'view_id', string='Companies')
