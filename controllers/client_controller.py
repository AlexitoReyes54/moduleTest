import json
from odoo import http, SUPERUSER_ID
from odoo.http import request


class RegisterUserController(http.Controller):
    @http.route(
        "/api/client",
        type="http",
        auth="none",
        cors="*",
        methods=["POST", "OPTIONS"],
        csrf=False,
    )
    def handler(self, **kwargs):
        data = kwargs
        if not data and request.httprequest.data:
            try:
                data = json.loads(request.httprequest.data)
            except Exception:
                data = {}

        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            error_payload = {
                "status": "error",
                "message": "Missing required fields: 'name' and 'email' are required.",
            }
            return request.make_response(
                json.dumps(error_payload),
                headers=[("Content-Type", "application/json")],
                status=400,  # Bad Request
            )

        new_client = (
            request.env["ecommerce.client"]
            .sudo()
            .create(
                {
                    "username": name,
                    "email": email,
                }
            )
        )

        response_payload = {
            "status": "success",
            "data": {
                "id": new_client.id,
                "name": new_client.username,
                "email": new_client.email,
            },
        }

        lead_vals = {
            "name": new_client.username,
            "contact_name": new_client.username,
            "email_from": new_client.email,
            "phone": "000",
            "description": "none",
            "type": "lead",
        }


        return request.make_response(
            json.dumps(response_payload),
            headers=[
                ("Content-Type", "application/json"),
                # ("Access-Control-Allow-Origin", "*"),
            ],
        )

    def _create_lead(request, name, email):
        pass
