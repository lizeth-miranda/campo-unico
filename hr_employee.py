# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class employees(models.Model):
    _inherit = 'hr.employee'

    _sql_constraints = [
        ('default_code_uniq', 'unique(identification_id)',
         "A default code can only be assigned to one product !"),
    ]
