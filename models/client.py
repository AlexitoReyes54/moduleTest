from odoo import models, fields, api


class client(models.Model):
    _name = "ecommerce.client"
    _description = "E-commerce Client"

    username = fields.Char(
        string="Username",
        required=True,
        index=True,
        copy=False,
        help="Unique identifier used as the sole login credential.",
    )
    email = fields.Char(string="Email")
    active = fields.Boolean(default=True)

    # Enforce uniqueness at the database level so credentials don't collide
    _sql_constraints = [
        ("username_unique", "unique(username)", "This username is already taken!")
    ]

    # 1:1 Cart Relationship (Virtual reverse lookup)
    # Since there's only 1 cart, limit=1 makes it behave like a single object instead of a list
    cart_id = fields.Many2one(
        comodel_name="ecommerce.cart", compute="_compute_cart_id", string="Active Cart"
    )

    def _compute_cart_id(self):
        for client in self:
            # Look up the single cart linked to this client
            client.cart_id = self.env["ecommerce.cart"].search(
                [("client_id", "=", client.id)], limit=1
            )

    # api external comunication
    @api.model
    def authenticate(self, username):
        """
        Validates the client based solely on the username.
        Returns the client record if found, otherwise False.
        """
        if not username:
            return False

        client = self.search([("username", "=", username)], limit=1)
        return client if client else False
