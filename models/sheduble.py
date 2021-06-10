# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Shedule(models.Model):

    _name = "shedule"
    _description = "Agenda"
    
    date_start = fields.Datetime(string="Horaire de début", required="True")
    date_stop = fields.Datetime(string="Horaire de fin", required="True")
    room = fields.Char(string="Salle de classe", required="True")
    
    class_id = fields.Many2one("class", required=True, ondelete='cascade', index=True, copy=False)
    course_id = fields.Many2one("course", required=True, ondelete='cascade', index=True, copy=False)
    