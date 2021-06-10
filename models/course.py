# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Course(models.Model):
    _name = "course"
    _description = "Cours"
    
    name = fields.Char(string="Matière", required="True")
    
    shedule_id = fields.One2many("agenda", "course_id")