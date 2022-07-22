from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(string="Active", default=True)
    lifespan = fields.Integer(string="Lifespan (day)", default=300, copy=False)

    def action_archive_record(self):
        check_all = True
        for record in self:
            if record.state not in ['done', 'cancel']:
                check_all = False
        if check_all:
            for record in self:
                record.active = False
        else:
            raise UserError('Need to lock or cancel purchase order')

    @api.model
    def delete_old_po(self):
        for po in self.search([("active", "=", True)]):
            if datetime.today() >= po.write_date + timedelta(days=po.lifespan):
                po.active = False
                
