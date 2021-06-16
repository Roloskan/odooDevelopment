# -*- coding: utf-8 -*-

from custom.diadema_modulo_impresoras.models.printer import printer, printerDetail
from odoo import models, fields, api

class createReport(models.TransientModel):
    _name = 'doff.printer.report.between.two.dates'
    _description = 'Crea un reporte personalizado dentro de un rango de fechas.'

    cutoff_date1 = fields.Date(string="Fecha inicial")
    cutoff_date2 = fields.Date(string="Fecha final")

    
    doff_printer_report_between_two_dates_detail_id = fields.One2many("doff.printer.report.between.two.dates.detail","doff_printer_report_between_two_dates_id", "doff_printer_report_between_two_dates_detail_id")

    @api.one
    def get_data(self):
        self.ensure_one()
        printer_data = self.env['doff.printer.detail'].search([
                                                        ('doff_printer_id.cutoff_date','>=',self.cutoff_date1),
                                                        ('doff_printer_id.cutoff_date','<=',self.cutoff_date2)])
        for rec in printer_data:
         obj_create = self.env["doff.printer.report.between.two.dates.detail"]
         obj_delete = self.env["doff.printer.report.between.two.dates.detail"].search([('doff_printer_report_between_two_dates_id','=',self.id)]).unlink()

         #Variables para obtener el total anual
         ftotal_c = 0
         ftotal_bw = 0

        #Asigno el total de impresiones segun la fecha, 01 = Enero; Numero de impresiones de ese mes: xx
        for rec in printer_data:
           date = rec.doff_printer_id.cutoff_date
           split = date.split("-")
           date = split[1]

           if date == "01":
               self.EneroC = rec.total_c
               self.EneroB = rec.total_bw
           if date == "02":
               self.FebreroC = rec.total_c
               self.FebreroB = rec.total_bw
           if date == "03":
               self.MarzoC = rec.total_c
               self.MarzoB = rec.total_bw
           if date == "04":
               self.AbrilC = rec.total_c
               self.AbrilB = rec.total_bw
           if date == "05":
               self.MayoC = rec.total_c
               self.MayoB = rec.total_bw
           if date == "06":
               self.JunioC = rec.total_c
               self.JunioB = rec.total_bw
           if date == "07":
               self.JulioC = rec.total_c
               self.JulioB = rec.total_bw
           if date == "08":
               self.AgostoC = rec.total_c
               self.AgostoB = rec.total_bw
           if date == "09":
               self.SeptiembreC = rec.total_c
               self.SeptiembreB = rec.total_bw
           if date == "10":
               self.OctubreC = rec.total_c
               self.OctubreB = rec.total_bw
           if date == "11":
               self.NoviembreC = rec.total_c
               self.NoviembreB = rec.total_bw
           if date == "12":
               self.DiciembreC = rec.total_c
               self.DiciembreB = rec.total_bw

        self.gran_total_color = ftotal_c
        self.gran_total_bw = ftotal_bw

        #Lleno el formulario creado en la vista.
        for rec1 in printer_data:
            vals_color = {
                "printer_model":rec1.printer_model,
                "printer_series":rec1.printer_series.printer_series,
                "department_name":rec1.department_name.department_name,
                "users_numbers":rec1.users_numbers,
                "EneroC":self.EneroC,
                "FebreroC":self.FebreroC,
                "MarzoC":self.MarzoC,
                "AbrilC":self.AbrilC,
                "MayoC":self.MayoC,
                "JunioC":self.JunioC,
                "JulioC":self.JulioC,
                "AgostoC":self.AgostoC,
                "SeptiembreC":self.SeptiembreC,
                "OctubreC":self.OctubreC,
                "NoviembreC":self.NoviembreC,
                "DiciembreC":self.DiciembreC,
                "gran_total_color":self.gran_total_color,
                "EneroB":self.EneroB,
                "FebreroB":self.FebreroB,
                "MarzoB":self.MarzoB,
                "AbrilB":self.AbrilB,
                "MayoB":self.MayoB,
                "JunioB":self.JunioB,
                "JulioB":self.JulioB,
                "AgostoB":self.AgostoB,
                "SeptiembreB":self.SeptiembreB,
                "OctubreB":self.OctubreB,
                "NoviembreB":self.NoviembreB,
                "DiciembreB":self.DiciembreB,
                "gran_total_bw":self.gran_total_bw,
                "doff_printer_report_between_two_dates_id":self.id
            }
        
        obj_create.create(vals_color)

class createReportDetail(models.TransientModel):
    _name = 'doff.printer.report.between.two.dates.detail'

    
    #Impresiones Color
    EneroC = fields.Integer("Enero (color)")
    FebreroC= fields.Integer("Febrero (color)")
    MarzoC = fields.Integer("Marzo (color)")
    AbrilC = fields.Integer("Abril (color)")
    MayoC = fields.Integer("Mayo (color)")
    JunioC = fields.Integer("Junio (color)")
    JulioC = fields.Integer("Julio (color)")
    AgostoC = fields.Integer("Agosto (color)")
    SeptiembreC = fields.Integer("Septiembre (color)")
    OctubreC = fields.Integer("Octubre (color)")
    NoviembreC = fields.Integer("Noviembre (color)")
    DiciembreC = fields.Integer("Diciembre (color)") 
    gran_total_color = fields.Integer("Total anual (color)")

    #Impresiones Blanco y Negro
    EneroB = fields.Integer("Enero (B/N)")
    FebreroB= fields.Integer("Febrero (B/N)")
    MarzoB = fields.Integer("Marzo (B/N)")
    AbrilB = fields.Integer("Abril (B/N)")
    MayoB = fields.Integer("Mayo (B/N)")
    JunioB = fields.Integer("Junio (B/N)")
    JulioB = fields.Integer("Julio (B/N)")
    AgostoB = fields.Integer("Agosto (B/N)")
    SeptiembreB = fields.Integer("Septiembre (B/N)")
    OctubreB = fields.Integer("Octubre (B/N)")
    NoviembreB = fields.Integer("Noviembre (B/N)")
    DiciembreB = fields.Integer("Diciembre (B/N)") 
    gran_total_bw = fields.Integer("Total anual (B/N)")   

    #Informacion General de las Impresoras
    printer_model = fields.Char("Modelo")
    printer_series = fields.Char('Serie')
    department_name = fields.Char("Ubicación")
    users_numbers = fields.Integer("Numero de usuarios")

    doff_printer_report_between_two_dates_id = fields.Many2one("doff.printer.report.between.two.dates","doff_printer_report_between_two_dates_id")

