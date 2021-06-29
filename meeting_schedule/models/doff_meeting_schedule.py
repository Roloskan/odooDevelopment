# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import AccessDenied, Warning

class meetingSchedule(models.Model):
    _name = 'doff.meeting.schedule'

    start_date = fields.Date("Fecha de inicio", default = fields.Datetime.now)
    location = fields.Char("Lugar")
    start_hour = fields.Float("Hora de inicio")
    end_hour = fields.Float("Hora final")
    responsable_id = fields.Many2one('res.users','Responsable', default=lambda self: self.env.uid)
    registration_date = fields.Date("Fecha de registro", default = fields.Datetime.now)

    doff_meeting_schedule_detail_id = fields.One2many("doff.meeting.schedule.detail","doff_meeting_schedule_id","doff_meeting_schedule_detail_id")
    doff_meeting_schedule_detail_id2 = fields.One2many("doff.meeting.schedule.detail2","doff_meeting_schedule_id2","doff_meeting_schedule_detail_id2")
    
class meetingEntry(models.Model):
    _name = 'doff.meeting.schedule.detail'

    people = fields.Many2one ('hr.employee','Nombre')

    doff_meeting_schedule_id = fields.Many2one("doff.meeting.schedule","doff_meeting_schedule_id")

class meetingEntry2(models.Model):
    _name = 'doff.meeting.schedule.detail2'
    topic = fields.Char('Tema')
    priority = fields.Selection([('Normal','Normal'),
                                ('Media','Media'),
                                ('Urdente','Urgente')],
                                'Prioridad', 
                                default="Normal")
    feedback = fields.Char('Comentarios')
    doff_meeting_schedule_id2 = fields.Many2one("doff.meeting.schedule","doff_meeting_schedule_id2")