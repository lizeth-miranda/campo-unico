# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models

class Product_produ(models.Model):
    _inherit = 'product.product'

    _sql_constraints = [
        ('default_code_uniq', 'unique(default_code)',
         "A default code can only be assigned to one product !"),
    ]
