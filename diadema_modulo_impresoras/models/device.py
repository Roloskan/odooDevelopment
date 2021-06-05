# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import Warning

#Gestionar impresoras
class device(models.Model):
    _name = 'doff.device'
    _rec_name = 'printer_series'

    partner_id = fields.Many2one('res.partner', string="Proveedor", required=True)
    printer_brand = fields.Char("Marca", required=True)
    printer_model =  fields.Char("Modelo", required=True)
    printer_series = fields.Char("Serie", required=True)
    paper_size = fields.Selection([('0', 'Carta'),
    ('1', 'Oficio'),
    ('2', 'Legal'),
    ('3', 'Oficio y Carta'),
    ('4', 'Carta, Oficio y Legal')],string="Tamaño de papel", required=True)
    paper_type =  fields.Char("Tipo de papel", required=True)
    users_numbers = fields.Integer("Numero de usuarios", required=True)
    department_name = fields.Many2one('doff.department', string="Ubicación", required=True)
