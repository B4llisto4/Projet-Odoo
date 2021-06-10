# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _name = "res.partner"
    _description = "Professeur"
    
    name = fields.Char(string="Prénom")
    class_ids = fields.Many2many("class", strinf="classe", required=True, ondelete='cascade', index=True, copy=False)