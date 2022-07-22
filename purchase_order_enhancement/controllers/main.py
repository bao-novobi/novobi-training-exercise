from odoo import http
from odoo.http import request, Response
import json


class Main(http.Controller):
    @http.route('/archive/test', type='json', auth='public', csrf=False)
    def books(self, **kwargs):
        data = json.loads(request.httprequest.data)
        order_id = data['params']['orders']
        records = request.env['purchase.order'].sudo().search(
            [("id", "in", order_id)])
        body = {
            "archived_orders": False,
            "code": 404,
            "message": "Could not found"
        }
        if len(records) == len(order_id):
            check_all = True
            for record in records:
                print(record.name)
                if record.state not in ['done', 'cancel']:
                    check_all = False
                    break
            if check_all:
                for record in records:
                    record.active = False
                body = {
                    "archived_orders": order_id,
                    "code": 200,
                    "message": "Successful"
                }
        return body
