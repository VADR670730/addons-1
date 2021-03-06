# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import date


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def write(self, vals):
        # vendor bills
        if (not self.date and not vals.get('date')
            and self.type in ('in_invoice', 'in_refund')):

            vals['date'] = date.today()

        return super(AccountInvoice, self).write(vals)
