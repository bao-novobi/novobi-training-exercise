from odoo import api, fields, models

class ArchivePurchaseOrdersWizard(models.TransientModel):
    _name = "archive.purchase.orders.wizard"

    purchase_order_id = fields.Many2many("purchase.order", string='Order Id', domain=[["active", "=", True]])

    def action_archive(self):
        self.purchase_order_id.action_archive_record()
        return