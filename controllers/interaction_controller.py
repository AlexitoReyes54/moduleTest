import json
from odoo import http
from odoo.http import request

class InteractionController(http.Controller):
    ALLOWED_EVENT_TYPES = ["login", "view_product", "add_to_cart", "custom_click"]

    @http.route(
        "/api/interaction", type="http", auth="public", methods=["POST"], csrf=False
    )
    def create_interaction(self, **kwargs):
        data = kwargs
        if not data and request.httprequest.data:
            try:
                data = json.loads(request.httprequest.data)
            except Exception:
                data = {}

        client_id = data.get("client_id")
        event_type = data.get("event_type")
        label = data.get("label")

        if not client_id or not event_type:
            return self._json_response(
                {
                    "status": "error",
                    "message": "Missing required fields: 'client_id' and 'event_type' are required.",
                },
                status=400,
            )

        if event_type not in self.ALLOWED_EVENT_TYPES:
            return self._json_response(
                {
                    "status": "error",
                    "message": f"Invalid 'event_type'. Must be one of: {', '.join(self.ALLOWED_EVENT_TYPES)}",
                },
                status=400,
            )

        client_exists = (
            request.env["ecommerce.client"].sudo().browse(int(client_id)).exists()
        )
        if not client_exists:
            return self._json_response(
                {
                    "status": "error",
                    "message": f"Client with ID {client_id} does not exist.",
                },
                status=404,
            )

        try:
            interaction = (
                request.env["ecommerce.interaction"]
                .sudo()
                .track(client_id=int(client_id), event_type=event_type, label=label)
            )
        except Exception as e:
            return self._json_response(
                {"status": "error", "message": str(e)}, status=500
            )

        response_payload = {
            "status": "success",
            "data": {
                "id": interaction.id,
            },
        }

        return self._json_response(response_payload, status=201)

    def _json_response(self, data, status=200):
        return request.make_response(
            json.dumps(data),
            headers=[("Content-Type", "application/json")],
            status=status,
        )
