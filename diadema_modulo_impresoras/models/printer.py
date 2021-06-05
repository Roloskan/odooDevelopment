# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import Warning

#Consumo de impresoras  
class printer(models.Model):
    _name = 'doff.printer'

    registration_date = fields.Date("Fecha de registro", default=fields.Datetime.now)
    responsable_id = fields.Many2one("res.users","Responsable", default=lambda self: self.env.uid)
    invoice_number = fields.Char("Numero de factura")
    cutoff_date = fields.Date("Fecha de corte")
    partner_id = fields.Many2one('res.partner', string="Proveedor", default=lambda self: self.env.uid)
    total_bill = fields.Float("Total de la factura")
    currency_id = fields.Many2one(
                'res.currency', 
                string='Divisa', 
                default=lambda self: self.env.uid, 
                domain=[('name', 'in', ('USD', 'DOP'))])
    
    doff_printer_detail_id = fields.One2many("doff.printer.detail","doff_printer_id", "doff_printer_detail_id")
    


class printerDetail(models.Model):
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


    printer_model = fields.Char("Modelo")
    printer_series = fields.Many2one('doff.device', 'Serie')
    department_name = fields.Many2one('doff.department', string="Ubicación")
    users_numbers = fields.Integer("Numero de usuarios")
    initial_bw = fields.Integer("Inicial B/N")
    final_bw = fields.Integer("Final B/N")
    total_bw = fields.Integer(string="Total B/N", compute='_get_res1')
    initial_c = fields.Integer("Inicial COLOR")
    final_c = fields.Integer("Final COLOR")
    total_c = fields.Integer(string="Total COLOR", compute='_get_res2')
    
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





