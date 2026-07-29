import json
from odoo import http
from odoo.http import request


class CartAPIController(http.Controller):
    @http.route(
        "/api/cart/add",
        type="http",
        auth="none",
        methods=["POST"],
        csrf=False,
    )
    def add_to_cart(self, **kwargs):
        body = json.loads(request.httprequest.data)
        client_id = int(body.get("client_id"))
        product_id = int(body.get("product_id"))

        Cart = request.env["ecommerce.cart"].sudo()
        CartItem = request.env["ecommerce.cart.item"].sudo()

        cart = Cart.search([("client_id", "=", client_id)], limit=1)
        if not cart:
            cart = Cart.create({"client_id": client_id})

        item = CartItem.search(
            [("cart_id", "=", cart.id), ("product_id", "=", product_id)],
            limit=1,
        )

        if not item:
            item = CartItem.create(
                {
                    "cart_id": cart.id,
                    "product_id": product_id,
                }
            )

        return request.make_response(
            json.dumps({"status": "success", "cart_id": cart.id, "item_id": item.id}),
            headers=[("Content-Type", "application/json")],
        )
