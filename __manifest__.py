{
    "name": "E-Commerce Watch",
    "summary": "Mock store implementation ",
    "description": """
        E-Commerce Custom Extension
    """,
    "author": "Alexander Reyes",
    "category": "E-Commerce",
    "version": "0.1",  # Update version based on your target Odoo instance
    "depends": [
        "base",
        "crm",
    ],
    "data": [
        "security/ir.model.access.csv",
        # "views/client_views.xml",
        # "views/interaction_views.xml",
        "views/watch_views.xml",
        "views/client_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
