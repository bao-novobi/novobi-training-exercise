from odoo import api, fields, models

class PurchaseOrderReport(models.Model):
    _inherit = 'purchase.report'

    payment_term_id = fields.Many2one('account.payment.term', 'Payment Terms', readonly=True)

    @api.model
    def _select(self):
        select_str = super(PurchaseOrderReport, self)._select() + ",po.payment_term_id as payment_term_id"
        return select_str

    @api.model
    def _group_by(self):
        group_by_str = super(PurchaseOrderReport, self)._group_by() + ",po.payment_term_id"
        return group_by_str
