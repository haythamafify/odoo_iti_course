from odoo import models, fields, api
from odoo.exceptions import ValidationError


class iti(models.Model):
    _name = 'iti'
    _description = 'iti'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(tracking=True)
    value = fields.Integer()
    value2 = fields.Float(readonly=True)
    value3 = fields.Float(compute="_compute_value3", store=True)
    value4 = fields.Integer()
    degree = fields.Integer()
    state = fields.Selection([('new', 'New'), ('confirmed', 'Confirmed'), ('fail', 'Fail'), ('graduated', 'Graduated'),
                              ('cancel', 'Cancel')], default="new")

    description = fields.Text()
    _sql_constraints = [
        ('unique_name',
         'UNIQUE(name)',
         'The name must be unique.')
    ]

    def action_confirm(self):
        # for rec in self:
        #     rec.state = "confirmed"
        self.state = "confirmed"

    def action_graduate(self):
        self.state = "graduated"

    @api.onchange("value")
    def on_change_vlaue(self):
        self.value2 = self.value / 3

    @api.depends("value")
    def _compute_value3(self):
        for rec in self:
            rec.value3 = float(rec.value / 100)

    @api.constrains("value4")
    def check_value4_less_than_200(self):
        if self.value4 > 200:
            raise ValidationError(" value 4 must be less than 200")
