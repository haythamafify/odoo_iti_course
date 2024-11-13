from odoo import models, fields, api


class Father(models.Model):
    _name = "father"

    name = fields.Char()
    son_ids = fields.One2many('son', 'father_id')
    # condition graduated or degree bigger than 60
    iti_id = fields.Many2one('iti', domain=["|", ('state', '=', 'graduated'), ('degree', '>', '60')])
