from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(string="Active", default=True)

    def action_archive_record(self, api_call=False):
        if self.env.user.has_group('purchase.group_purchase_manager') or api_call:
            check_state = self.filtered(lambda po: po.state not in ['done', 'cancel'])
            if check_state:
                raise UserError("Purchase orders state need to be locked or cancel in order to be archived.")
            else:
                self.write({'active': False})
        else:
            raise UserError('You do not have access to this function.')

    @api.model
    def archive_old_po(self):
        lifespan = int(self.env['ir.config_parameter'].sudo().get_param('purchase_order_enhancement.lifespan'))
        time_check = datetime.today() - timedelta(days=lifespan)
        old_pos = self.search([("write_date", "<=", time_check), ("state", "in", ['done', 'cancel'])])
        old_pos.write({"active": False})
        