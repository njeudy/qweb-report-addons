# -*- coding: utf-8 -*-

from openerp import models, fields


class irUiViewTheme(models.Model):

    _name = 'ir.ui.view.theme'

    name = fields.Char('Theme name')
    description = fields.Text('Description')
    view_ids = fields.One2many('ir.ui.view', 'view_theme_id', string='Associated views')
