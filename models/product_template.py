# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models

class product_temple(models.Model):
    _inherit = 'product.template'

    _sql_constraints = [
        ('default_code_uniq', 'unique(default_code)',
         "A default code can only be assigned to one product !"),
    ]
