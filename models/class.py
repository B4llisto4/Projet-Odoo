# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Class(models.Model):
    _name = "class"
    _description = "Classe"
    
    selection_list = [
        ("1", "Seconde"),
        ("2", "Première"),
        ("2", "Terminale"),
    ]
    
    name = fields.Char(string="Classe", required="True")
    level = fields.Selection(selection_list, string="Section de classe" required="True")
    teacher_ids = fields.Many2one("res.partner", required=True, ondelete='cascade', index=True, copy=False)
    student_id = fields.One2many("student", "class_id", required=True, ondelete='cascade', index=True, copy=False)
    student_nb = fields.Integer(compute="compute_counting_students", string="Nombre d'élèves")
    
    
    @api.depends('student_id')
    def compute_counting_students(self):
    
    compteurStudent = 0
    for Class in self:
        if Class.student_id !=0:
            for student in Class.student_id:
                computeurStudent+=1
        Class.student_nb = compteurStudent