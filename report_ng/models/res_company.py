# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ResCompany(models.Model):

    _inherit = 'res.company'

    @api.multi
    def apply_company_qweb_theme(self, view_theme_id):
        for record in self:
            views_to_activate = self.env['ir.ui.view'].search(['&', '&', ('view_theme_id', '=', view_theme_id),
                                                                         ('type', '=', 'qweb'),
                                                                    '|', ('active', '=', False),
                                                                         ('company_ids', 'not in', [self.env.user.company_id.id])])
            views_to_desactivate = self.env['ir.ui.view'].search([('view_theme_id', 'not in', [False, view_theme_id]),
                                                                  ('type', '=', 'qweb'),
                                                                  ('active', '=', True)])
            for view in views_to_activate:
                activated_company_ids = view.company_ids | record.search([('name', '=', record.name)])
                view.write({'active': True,
                            'company_ids': [(6, 0, activated_company_ids.ids)],
                            })
            for view in views_to_desactivate:
                desactivated_company_ids = view.company_ids - record.search([('name', '=', record.name)])
                vals = {'company_ids': [(6, 0, desactivated_company_ids.ids)]}
                if not desactivated_company_ids:
                    vals.update({'active': False})
                view.write(vals)
            return True

    @api.multi
    def write(self, vals):
        res = super(ResCompany, self).write(vals)
        self.apply_company_qweb_theme(vals.get('view_theme_id', False))
        return res

    color = fields.Char(string="Color", help="Choose your color")
    view_theme_id = fields.Many2one('ir.ui.view.theme', string="Theme")
