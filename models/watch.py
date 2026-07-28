from odoo import models, fields

class watch(models.Model):
    _name = "product.watch"
    _description = "man item"

    reference = fields.Char()
    name = fields.Char()
    family = fields.Char()
    brand = fields.Selection(
        selection=[
            ("rolex", "Rolex"),
            ("omega", "Omega"),
            ("hamilton", "Hamilton"),
            ("patek_philippe", "Patek Philippe"),
            ("tissot", "Tissot"),
            ("panerai", "Panerai"),
        ],
        string="brand",
        required=True,
        index=True,
    )

    movement = fields.Char()
    limited = fields.Boolean()
    image = fields.Char()
    description = fields.Char()
