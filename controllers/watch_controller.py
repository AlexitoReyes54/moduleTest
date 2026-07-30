import json
from odoo import http


class getWatchController(http.Controller):
    @http.route(
        "/api/watches",
        type="http",
        auth="none",
        methods=["GET", "OPTIONS"],
        cors="*",
        csrf=False,
    )
    def handler(self):
        items = http.request.env["product.watch"].sudo().search([])

        data = [
            {
                "id": item.id,
                "display_name": item.name,
                "brand": item.brand,
                "movement": item.movement,
                "limited": item.limited,
                "image": item.image,
                "description": item.description,
            }
            for item in items
        ]

        payload = {
            "count": len(items),
            "data": data,
        }

        return http.request.make_response(
            json.dumps(payload),
            headers=[
                ("Content-Type", "application/json"),
                #("Access-Control-Allow-Origin", "*"),
            ],
        )
