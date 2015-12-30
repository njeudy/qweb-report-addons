# -*- coding: utf-8 -*-

from openerp.osv import osv
import babel.numbers
import decimal

class Report(osv.Model):
    _name = "report"
    _inherit = "report"

    def render(self, cr, uid, ids, template, values=None, context=None):
        """Allow to render a QWeb template python-side. This function returns the 'ir.ui.view'
        render but embellish it with some variables/methods used in reports.

        :param values: additionnal methods/variables used in the rendering
        :returns: html representation of the template
        """

        def group_by(elts, key):
            heaps = {}
            for elt in elts:
                k = key(elt)
                heaps[k] = heaps.get(k, []) + [elt]
            return heaps

        def escape_xml(str):
            return str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        def format_decimal(amount, lang=None, format='#,##0.00', **kwargs):
            """Format any amount in the given format and locale
            >>> format_decimal('2813.7456', lang='en')
            '2,813.74'
            >>> format_decimal('2813.7456', lang='fr')
            '2 813,74'
            >>> format_decimal('2813.7456', lang='fr', format='#,###0.000')
            '2813,746'
            """

            return babel.numbers.format_decimal(
                decimal.Decimal(amount), format=format,
                locale=lang, **kwargs)

        values.update({'group_by': group_by,
                       'format_decimal': format_decimal,
                       'sorted': sorted})

        return super(Report, self).render(cr, uid, ids, template=template, values=values, context=context)
