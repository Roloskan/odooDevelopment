# -*- coding: utf-8 -*-

from odoo import models, fields


class createReport(models.TransientModel):
    _name = 'create.printer.report'
    _description = 'Crear un reporte personalizado'

    printer_date1 = fields.Date(string="Fecha de inicio")
    printer_date2 = fields.Date(string="Fecha final")
    
    def get_data(self):
        create_report = self.env['create.printer.report'].search([])

        #Obtengo la informacion del modelo doff.printer dentro del rango de fechas.
        for rec2 in create_report:     
            printer = self.env['doff.printer'].search([('cutoff_date','>=',rec2.printer_date1),('cutoff_date','<=',rec2.printer_date2)])

        for r2 in printer.doff_printer_detail_ids:
           print("Pruebaaaaaaaaaa")

        total_bill = 0.0;

        #Realizo operaciones con los valores obtenidos en rec2
        for rec in printer: 
            print("rec:", rec.cutoff_date)
            total_bill = float(total_bill + rec.total_bill)
        
        print(total_bill)
        return{
            "type": "ir.actions.do_nothing"
        }