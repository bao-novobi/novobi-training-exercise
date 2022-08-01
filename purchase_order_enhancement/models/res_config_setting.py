from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lifespan = fields.Integer(string="Lifespan", default=100)

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('purchase_order_enhancement.lifespan', self.lifespan)
        return res
    
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        lifespan = self.env['ir.config_parameter'].sudo().get_param('purchase_order_enhancement.lifespan')
        res.update(lifespan = lifespan)
        return res