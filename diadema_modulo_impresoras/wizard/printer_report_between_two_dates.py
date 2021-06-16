# -*- coding: utf-8 -*-

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

            veri = self.env["doff.printer.report.between.two.dates.detail"].search([('doff_printer_report_between_two_dates_id','=',self.id),
                                                                                    ('printer_series','=',rec.printer_series.printer_series)])
           
            if not veri:

                vals_color = {
                    "printer_model":rec.printer_model,
                    "printer_series":rec.printer_series.printer_series,
                    "department_name":rec.department_name.department_name,
                    "users_numbers":rec.users_numbers,
                    "doff_printer_report_between_two_dates_id":self.id
                }

                if date == "01":
                    vals_color["EneroC"] = rec.total_c
                    vals_color["EneroB"] = rec.total_bw
                
                if date == "02":
                    vals_color["FebreroC"] = rec.total_c
                    vals_color["FebreroB"] = rec.total_bw
                
                if date == "03":
                    vals_color["MarzoC"] = rec.total_c
                    vals_color["MarzoB"] = rec.total_bw
                if date == "04":
                    vals_color["AbrilC"] = rec.total_c
                    vals_color["AbrilB"] = rec.total_bw
                
                if date == "05":
                    vals_color["MayoC"] = rec.total_c
                    vals_color["MayoB"] = rec.total_bw
                
                if date == "06":
                    vals_color["JunioC"] = rec.total_c
                    vals_color["JunioB"] = rec.total_bw
                
                if date == "07":
                    vals_color["JulioC"] = rec.total_c
                    vals_color["JulioB"] = rec.total_bw
                
                if date == "08":
                    vals_color["AgostoC"] = rec.total_c
                    vals_color["AgostoB"] = rec.total_bw
                
                if date == "09":
                    vals_color["SeptiembreC"] = rec.total_c
                    vals_color["SeptiembreB"] = rec.total_bw
                
                if date == "10":
                    vals_color["OctubreC"] = rec.total_c
                    vals_color["OctubreB"] = rec.total_bw
                
                if date == "11":
                    vals_color["NoviembreC"] = rec.total_c
                    vals_color["NoviembreB"] = rec.total_bw
                
                if date == "12":
                    vals_color["DiciembreC"] = rec.total_c
                    vals_color["DiciembreB"] = rec.total_bw

                obj_create.create(vals_color)
               
            else:

                if date == "01":
                    veri.EneroC += rec.total_c
                    veri.EneroB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "02":
                    veri.FebreroC += rec.total_c
                    veri.FebreroB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "03":
                    veri.MarzoC += rec.total_c
                    veri.MarzoB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw

                if date == "04":
                    veri.AbrilC += rec.total_c
                    veri.AbrilB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "05":
                    veri.MayoC += rec.total_c
                    veri.MayoB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "06":
                    veri.JunioC += rec.total_c
                    veri.JunioB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "07":
                    veri.JulioC += rec.total_c
                    veri.JulioB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "08":
                    veri.AgostoC += rec.total_c
                    veri.AgostoB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "09":
                    veri.SeptiembreC += rec.total_c
                    veri.SeptiembreB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "10":
                    veri.OctubreC += rec.total_c
                    veri.OctubreB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "11":
                    veri.NoviembreC += rec.total_c
                    veri.NoviembreB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
                
                if date == "12":
                    veri.DiciembreC += rec.total_c
                    veri.DiciembreB += rec.total_bw
                    veri.gran_total_color +=  rec.total_c
                    veri.gran_total_bw +=  rec.total_bw
        

class createReportDetail(models.TransientModel):
    _name = 'doff.printer.report.between.two.dates.detail'

    cutoff_date = fields.Date("Fecha de corte")
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

