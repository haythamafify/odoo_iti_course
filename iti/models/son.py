from odoo import models, fields


class Son(models.Model):
    _name = "son"

    son_name = fields.Char()
    father_id = fields.Many2one('father')
