from odoo import models, fields, api

class cart(models.Model):
    _name = "ecommerce.cart"
    _description = "E-commerce Shopping Cart"

    client_id = fields.Many2one(
        comodel_name="ecommerce.client",
        string="Client",
        required=True,
        ondelete="cascade",
        index=True,
    )

    item_ids = fields.One2many(
        comodel_name="ecommerce.cart.item",
        inverse_name="cart_id",
        string="Cart Items",
    )

    _sql_constraints = [
        ("client_unique", "unique(client_id)", "A client can only have one cart!")
    ]


# todo: create a cart line model and update the way it works
class cartItem(models.Model):
    _name = "ecommerce.cart.item"
    _description = "E-commerce Shopping Cart item"

    cart_id = fields.Many2one(
        comodel_name="ecommerce.cart",
        string="Cart",
        required=True,
        ondelete="cascade",
        index=True,
    )

    product_id = fields.Many2one(
        comodel_name="product.watch",
        string="Watch Product",
        required=True,
        ondelete="cascade",
    )

    _sql_constraints = [
        (
            "cart_product_unique",
            "unique(cart_id, product_id)",
            "This watch is already in the cart! Increase quantity instead.",
        )
    ]
