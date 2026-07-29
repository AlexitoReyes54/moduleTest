from odoo import http


class MyController(http.Controller):
    @http.route("/t", auth="public")
    def handler(self):
        return "hello buddy"
