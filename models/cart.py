from odoo import models, fields, api


class cart(models.Model):
    _name = "ecommerce.cart"
    _description = "E-commerce Shopping Cart"

    # Foreign Key pointing to Client
    client_id = fields.Many2one(
        comodel_name="ecommerce.client",
        string="Client",
        required=True,
        ondelete="cascade",
        index=True,
    )

    # watch relationship
    product_id = fields.Many2one(
        comodel_name="product.watch", string="Product", required=False
    )

    # THIS IS THE KEY TO 1:1
    # SQL Constraint prevents the same client_id from ever appearing twice in this table
    _sql_constraints = [
        ("client_unique", "unique(client_id)", "A client can only have one cart!")
    ]
