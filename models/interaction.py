from odoo import models, fields, api

class EcommerceInteraction(models.Model):
    _name = "ecommerce.interaction"
    _description = "E-commerce User Interaction Log"
    _order = "timestamp desc"

    client_id = fields.Many2one(
        comodel_name="ecommerce.client",
        string="Client",
        required=True,
        ondelete="cascade",
        index=True,
    )

    event_type = fields.Selection(
        [
            ("login", "Login"),
            ("view_product", "Product View"),
            ("add_to_cart", "Add to Cart"),
            ("custom_click", "Custom Click"),
        ],
        string="Event Type",
        required=True,
        index=True,
    )

    # UI details: what element or label they interacted with
    label = fields.Char(
        string="Element / Label",
        help="Context on what was clicked (e.g., 'Hero CTA Banner', 'Buy Now Button')",
    )

    # Automatic timestamping
    timestamp = fields.Datetime(
        string="Timestamp",
        default=fields.Datetime.now,
        required=True,
        readonly=True,
    )

    @api.model
    def track(self, client_id, event_type, label=None):
        return self.create(
            {
                "client_id": client_id,
                "event_type": event_type,
                "label": label,
            }
        )
