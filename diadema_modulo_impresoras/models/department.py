# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import Warning

#Gestionar departamentos
class department(models.Model):
    _name = 'doff.department'
    _rec_name = 'department_name'

    department_name = fields.Char("Nombre", required= True)
    department_location =  fields.Char("Ubicación", required= True)

doff_department_id = fields.One2many("department_name", "doff_department_id")
