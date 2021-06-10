# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class Student(models.Model):
    _name = "student"
    _description = "Elève"
    
    firstname = fields.Char(string="Prénom", required="True")
    lastname = fields.Char(string="Nom", required="True")
    birthdate = fields.Date(string="Date de naissance")
    age = fields.Integer(compute="compute_age_student", store="True" string="Age")
    class_id = fields.Many2one("class", required=True, ondelete='cascade', index=True, copy=False)
    
    
    @api.depends('birthdate')
    def compute_age_student(self):
    
        todayDate = date.today()
        
        for element in self:
            if(element.birthdate !=0):
                element.age = (todayDate - element.birthdate).days/365