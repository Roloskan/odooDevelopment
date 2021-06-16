# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class contratoEmpleado(models.Model):

    _name = 'doff.contrato'

    r_employee_id = fields.Many2one('hr.employee', string='Employee')
    r_department_id = fields.Many2one('hr.department', string="Department")
    r_job_id = fields.Many2one('hr.job', string='Job Position')
    r_date_start = fields.Date('Start Date', required=True, default=fields.Date.today)
    r_resource_calendar_id = fields.Many2one(
        'resource.calendar', 'Working Schedule',
        default=lambda self: self.env['res.company']._company_default_get().resource_calendar_id.id)


    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            print(self.r_job_id)
            self.r_job_id = self.employee_id.job_id
            self.r_department_id = self.employee_id.department_id
            self.r_resource_calendar_id = self.employee_id.resource_calendar_id