from odoo import models, fields, api
from odoo.exceptions import AccessDenied, Warning


class configuration(models.Model):
    _name = 'doff.configuration'

    @api.onchange('default_input_a')
    def onchange_default_input_a(self):
        if self.default_input_a:
            self.default_input_ab = self.default_input_a.lot_stock_id.id

    @api.onchange('default_internal_a')
    def onchange_default_internal_a(self):
        if self.default_internal_a:
            self.default_internal_ab = self.default_internal_a.lot_stock_id.id

    @api.onchange('default_output_a')
    def onchange_default_output_a(self):
        if self.default_output_a:
            self.default_output_ab = self.default_output_a.lot_stock_id.id



    default_input_a = fields.Many2one("stock.warehouse", string="Almacen", default = lambda self: self.env['stock.warehouse'].search([('company_id', '=', self.env.user.company_id.id)], limit=1))
    default_input_ab = fields.Many2one("stock.location", string="Ubicacion")
    default_internal_a = fields.Many2one("stock.warehouse", string="Almacen", default = lambda self: self.env['stock.warehouse'].search([('company_id', '=', self.env.user.company_id.id)], limit=1))
    default_internal_ab = fields.Many2one("stock.location", string="Ubicacion")
    default_output_a = fields.Many2one("stock.warehouse", string="Almacen", default = lambda self: self.env['stock.warehouse'].search([('company_id', '=', self.env.user.company_id.id)], limit=1))
    default_output_ab = fields.Many2one("stock.location", string="Ubicacion")