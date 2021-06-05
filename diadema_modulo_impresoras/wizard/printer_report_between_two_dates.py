# -*- coding: utf-8 -*-

from custom.diadema_modulo_impresoras.models.printer import printer, printerDetail
from odoo import models, fields

class createReport(models.TransientModel):
    _name = 'doff.printer.report.between.two.dates'
    _description = 'Crea un reporte personalizado dentro de un rango de fechas.'

    cutoff_date1 = fields.Date(string="Fecha inicial")
    cutoff_date2 = fields.Date(string="Fecha final")

    
    doff_printer_report_between_two_dates_detail_id = fields.One2many("doff.printer.report.between.two.dates.detail","doff_printer_report_between_two_dates_id", "doff_printer_report_between_two_dates_detail_id")

    def get_data(self):
        printer_data = self.env['doff.printer'].search([('cutoff_date','>=',self.cutoff_date1),
                                                        ('cutoff_date','<=',self.cutoff_date2)])
        
        obj_create = self.env["doff.printer.report.between.two.dates.detail"]
        obj_delete = self.env["doff.printer.report.between.two.dates.detail"].search([('doff_printer_report_between_two_dates_id','=',self.id)]).unlink()

        #Variables para obtener el total anual
        ftotal_c = 0
        ftotal_bw = 0

        #Asigno el total de impresiones segun la fecha, 01 = Enero; Numero de impresiones de ese mes: xx
        for rec in printer_data:
           date = rec.cutoff_date
           split = date.split("-")
           date = split[1]
           ftotal_c += rec.doff_printer_detail_id.total_c
           ftotal_bw += rec.doff_printer_detail_id.total_bw

           if date == "01":
               self.EneroC = rec.doff_printer_detail_id.total_c
               self.EneroB = rec.doff_printer_detail_id.total_bw
           if date == "02":
               self.FebreroC = rec.doff_printer_detail_id.total_c
               self.FebreroB = rec.doff_printer_detail_id.total_bw
           if date == "03":
               self.MarzoC = rec.doff_printer_detail_id.total_c
               self.MarzoB = rec.doff_printer_detail_id.total_bw
           if date == "04":
               self.AbrilC = rec.doff_printer_detail_id.total_c
               self.AbrilB = rec.doff_printer_detail_id.total_bw
           if date == "05":
               self.MayoC = rec.doff_printer_detail_id.total_c
               self.MayoB = rec.doff_printer_detail_id.total_bw
           if date == "06":
               self.JunioC = rec.doff_printer_detail_id.total_c
               self.JunioB = rec.doff_printer_detail_id.total_bw
           if date == "07":
               self.JulioC = rec.doff_printer_detail_id.total_c
               self.JulioB = rec.doff_printer_detail_id.total_bw
           if date == "08":
               self.AgostoC = rec.doff_printer_detail_id.total_c
               self.AgostoB = rec.doff_printer_detail_id.total_bw
           if date == "09":
               self.SeptiembreC = rec.doff_printer_detail_id.total_c
               self.SeptiembreB = rec.doff_printer_detail_id.total_bw
           if date == "10":
               self.OctubreC = rec.doff_printer_detail_id.total_c
               self.OctubreB = rec.doff_printer_detail_id.total_bw
           if date == "11":
               self.NoviembreC = rec.doff_printer_detail_id.total_c
               self.NoviembreB = rec.doff_printer_detail_id.total_bw
           if date == "12":
               self.DiciembreC = rec.doff_printer_detail_id.total_c
               self.DiciembreB = rec.doff_printer_detail_id.total_bw

        self.gran_total_color = ftotal_c
        self.gran_total_bw = ftotal_bw

        #Lleno el formulario creado en la vista.
        for rec1 in printer_data:
            vals_color = {
                "printer_model":rec1.doff_printer_detail_id.printer_model,
                "printer_series":rec1.doff_printer_detail_id.printer_series.printer_series,
                "department_name":rec1.doff_printer_detail_id.department_name.department_name,
                "users_numbers":rec1.doff_printer_detail_id.users_numbers,
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
                "doff_printer_report_between_two_dates_id":self.id
            }


            vals_bw = {
                "printer_model":rec1.doff_printer_detail_id.printer_model,
                "printer_series":rec1.doff_printer_detail_id.printer_series.printer_series,
                "department_name":rec1.doff_printer_detail_id.department_name.department_name,
                "users_numbers":rec1.doff_printer_detail_id.users_numbers,
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
    EneroC = fields.Integer("Enero")
    FebreroC= fields.Integer("Febrero")
    MarzoC = fields.Integer("Marzo")
    AbrilC = fields.Integer("Abril")
    MayoC = fields.Integer("Mayo")
    JunioC = fields.Integer("Junio")
    JulioC = fields.Integer("Julio")
    AgostoC = fields.Integer("Agosto")
    SeptiembreC = fields.Integer("Septiembre")
    OctubreC = fields.Integer("Octubre")
    NoviembreC = fields.Integer("Noviembre")
    DiciembreC = fields.Integer("Diciembre") 
    gran_total_color = fields.Integer("Total anual")

    #Impresiones Blanco y Negro
    EneroB = fields.Integer("EneroB")
    FebreroB= fields.Integer("FebreroB")
    MarzoB = fields.Integer("MarzoB")
    AbrilB = fields.Integer("AbrilB")
    MayoB = fields.Integer("MayoB")
    JunioB = fields.Integer("JunioB")
    JulioB = fields.Integer("JulioB")
    AgostoB = fields.Integer("AgostoB")
    SeptiembreB = fields.Integer("SeptiembreB")
    OctubreB = fields.Integer("OctubreB")
    NoviembreB = fields.Integer("NoviembreB")
    DiciembreB = fields.Integer("DiciembreB") 
    gran_total_bw = fields.Integer("Total anual")   

    #Informacion General de las Impresoras
    printer_model = fields.Char("Modelo")
    printer_series = fields.Char('Serie')
    department_name = fields.Char("Ubicación")
    users_numbers = fields.Integer("Numero de usuarios")

    doff_printer_report_between_two_dates_id = fields.Many2one("doff.printer.report.between.two.dates","doff_printer_report_between_two_dates_id")

