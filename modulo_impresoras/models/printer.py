# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import Warning

#Consumo de impresoras  
class printer(models.TransientModel):
    _name = 'doff.printer'
    _inherits = {'res.partner': 'partner_id'}
    _inherits = {'res.currency': 'currency_id'}

    registration_date = fields.Date("Fecha de registro", default=fields.Datetime.now)
    responsable_id = fields.Many2one("res.users","Responsable", default=lambda self: self.env.uid)
    invoice_number = fields.Char("Numero de factura")
    cutoff_date = fields.Date("Fecha de corte")
    partner_id = fields.Many2one('res.partner', string="Proveedor", required=True, ondelete='cascade')
    total_bill = fields.Float("Total de la factura")
    currency_id = fields.Many2one(
                'res.currency', 
                string='Divisa', 
                required=True, 
                domain=[('name', 'in', ('USD', 'DOP'))])
    
    doff_printer_detail_ids = fields.One2many("doff.printer.detail","doff_printer_id", "doff_printer_detail_ids")
    


class printerDetail(models.TransientModel):
    _name = 'doff.printer.detail'
    
    #Funcion para seleccionar automaticamente los campos vinculados a printer_series.
    @api.onchange('printer_series')
    def set_values(self):
        for rec in self:
            if rec.printer_series:
                rec.printer_brand = rec.printer_series.printer_brand
                rec.printer_model = rec.printer_series.printer_model
                rec.department_name = rec.printer_series.department_name
                rec.paper_size = rec.printer_series.paper_size
                rec.paper_type = rec.printer_series.paper_type
                rec.users_numbers = rec.printer_series.users_numbers


    printer_model = fields.Char("MODELO")
    printer_series = fields.Many2one('doff.device', 'SERIE')
    department_name = fields.Many2one('doff.department', string="Ubicación", required=True, ondelete='cascade')
    users_numbers = fields.Integer("NUMERO DE USUARIOS")
    initial_bw = fields.Integer("INICIAL B/N")
    final_bw = fields.Integer("FINAL B/N")
    total_bw = fields.Integer(string="TOTAL B/N", compute='_get_res1')
    initial_c = fields.Integer("INICIAL COLOR")
    final_c = fields.Integer("FINAL COLOR")
    total_c = fields.Integer(string="TOTAL COLOR", compute='_get_res2')
    gran_total_bw = fields.Integer("Total color")

    #Funcion para calcular el total de impresiones en blanco y negro.
    @api.depends('initial_bw', 'final_bw')
    def _get_res1(self):
        for rec in self:
          rec.total_bw = rec.final_bw - rec.initial_bw

    #Funcion para calcular el total de impresiones a color.
    @api.depends('initial_c', 'final_c')
    def _get_res2(self):
        for rec in self:
          rec.total_c = rec.final_c - rec.initial_c

    doff_printer_id = fields.Many2one("doff.printer","doff_printer_id")





