# -*- coding: utf-8 -*-

from odoo import models, fields


class createReport(models.TransientModel):
    _name = 'create.printer.report'
    _description = 'Crea un reporte personalizado dentro de un rango de fechas.'

    cutoff_date1 = fields.Date(string="Fecha de inicio")
    cutoff_date2 = fields.Date(string="Fecha final")
    
    def get_data(self):
        create_report = self.env['create.printer.report'].search([])

        #Obtengo la informacion del modelo doff.printer dentro del rango de fechas.
        for rec2 in create_report:     
            printer = self.env['doff.printer'].search([('cutoff_date','>=',rec2.cutoff_date1),('cutoff_date','<=',rec2.cutoff_date2)])


        for r2 in printer.doff_printer_detail_ids:
            print(r2.cutoff_date)
            print(printer_model = r2.printer_model)
            print(printer_series = r2.printer_series)
            print(department_name = r2.department_name)
            print(total_bw = r2.total_bw)
            print(total_c = r2.printer_model)