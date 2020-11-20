# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class product_temple(models.Model):
    _inherit = 'product.template'

    campo_unico = fields.Char(
        string="Campo Unico",
    )

    _sql_constraints = [
        ('campo_unico_uniq', 'unique(campo_unico)',
         "La Referencia Interna que se intenta agregar, ya existe !"),
    ]
