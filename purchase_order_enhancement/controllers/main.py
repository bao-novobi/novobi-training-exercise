from warnings import catch_warnings
from odoo import http
from odoo.http import request
import json


class Main(http.Controller):
    @http.route('/archive/test', type='json', auth='public', csrf=False)
    def archive(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
        except:
            body = {
                "archived_orders": False,
                "code": 400,
                "message": "Invalid Request"
            }
            return body
        method = data.get('params').get('method')
        order_ids = data.get('params').get('orders')
        if method != "archive":
            body = {
                "archived_orders": False,
                "code": 400,
                "message": "Invalid Method"
            }
        elif not isinstance(order_ids, list) or not all([isinstance(x, int) for x in order_ids]):
            body = {
                "archived_orders": False,
                "code": 400,
                "message": "Invalid Purchase Order Ids"
            }
        else:
            records = request.env['purchase.order'].sudo().browse(order_ids).exists()
            body = {
                "archived_orders": False,
                "code": 404,
                "message": "Could not find the Purchase Order ids"
            }
            if len(records) == len(order_ids):
                try:
                    records.action_archive_record(True)
                except:
                    body = {
                        "archived_orders": False,
                        "code": 406,
                        "message": "Cannot archive"
                    }
                    return body
                body = {
                    "archived_orders": order_ids,
                    "code": 200,
                    "message": "Successful"
                }
        return body
