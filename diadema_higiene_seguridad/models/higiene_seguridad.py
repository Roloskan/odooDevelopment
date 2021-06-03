# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models, fields, api
from odoo.exceptions import Warning


#Encabezado
class higieneSeguridad(models.Model):
    _name = 'doff.higiene.seguridad'

    #Botones Borrador, Transito, Aprobado.
    @api.multi
    def btn_borrador(self):
        for rec in self:
            rec.write({'state': 'Borrador'})
    
    @api.multi
    def btn_transito(self):
        for rec in self:
            rec.write({'state': 'Transito'})

    
    @api.multi
    def btn_aprobado(self):
        for rec in self:
            rec.write({'state': 'Aprobado'})

    @api.onchange('type_of_operation')
    def onchange_type_of_operation(self):
        if self.type_of_operation:
            print("gola")

    #Evento para obtener el stock_id y location_id segun el warehouse de origen.
    @api.onchange('storage')
    def onchange_storage(self):
        if self.storage:
            self.stock_id = self.storage.lot_stock_id.id
            self.location = self.storage.lot_stock_id.id

    #Evento para obtener el stock_id y location_id segun el warehouse destino.
    @api.onchange('storage_destino')
    def onchange_storage_destino(self):
        if self.storage_destino:
            self.stock_id = self.storage_destino.lot_stock_id.id
            self.location_destino = self.storage_destino.lot_stock_id.id

    registration_date = fields.Date("Fecha de registro", default=fields.Datetime.now)
    responsable_id = fields.Many2one("res.users","Responsable", default=lambda self: self.env.uid)
    storage = fields.Many2one("stock.warehouse", string="Almacen origen", default= lambda self: self.env.uid)
    location = fields.Many2one("stock.location", string="Ubicación origen")
    storage_destino = fields.Many2one("stock.warehouse", string="Almacen destino", default= lambda self: self.env.uid)
    location_destino = fields.Many2one("stock.location", string="Ubicación destino")
    type_of_operation = fields.Selection([('Entrada','Entrada'), 
                                          ('Interno','Interno'), 
                                          ('Salida','Salida')], 
                                          string="Tipo", 
                                          default="Entrada"
                                        )
    stock_id = fields.Many2one("stock.location","Stock location")
    state = fields.Selection([('Borrador','Borrador'),
                              ('Transito','Transito'),
                              ('Aprobado','Aprobado')],
                              'Estado', 
                              default="Borrador"
                            )
    
    doff_higiene_seguridad_detail_id = fields.One2many("doff.higiene.seguridad.detail", "doff_higiene_seguridad_id", "doff_higiene_seguridad_detail_id")

#Detalle
class higieneSeguridadDetail(models.Model):
    _name = 'doff.higiene.seguridad.detail'
    
    #Evento para obtener el inventario disponible para el producto seleccionado.
    @api.onchange('product_higiene_seguridad')
    def onchange_product_higiene_seguridad(self):
            for rec in self:
                #Funcion if para verificar el tipo de operacion y segun esta ultima verificar que ubicacion debe tomar en cuenta.
                if rec.doff_higiene_seguridad_id.type_of_operation == 'Entrada':
                    if rec.product_higiene_seguridad:
                        stock = self.env['stock.quant'].search([('product_id','=',rec.product_higiene_seguridad.id),
                                                                ('location_id','=',rec.doff_higiene_seguridad_id.location_destino.id)], limit = 1)
                        rec.qty_available = stock.quantity
                else:
                        stock = self.env['stock.quant'].search([('product_id','=',rec.product_higiene_seguridad.id),
                                                                ('location_id','=',rec.doff_higiene_seguridad_id.location.id)], limit = 1)
                        rec.qty_available = stock.quantity
    
    #Evento para verificar que la cantidad no sea superior a la cantidad disponible para los movimientos Interno y Salida.
    @api.onchange('qty')
    def onchange_qty(self):
        for rec in self:
            if rec.qty>rec.qty_available and rec.doff_higiene_seguridad_id.type_of_operation != "Entrada":
                rec.qty = 0
                return {
		            'warning': {'title': "Alerta", 'message': "La cantidad no puede ser superior a la cantidad disponible."},
                }

    product_higiene_seguridad = fields.Many2one("product.product","Productos", domain="[('product_higiene_seguridad_check','=',True)]")
    qty_available = fields.Integer(string="Cantidad disponible",store=True,readonly=True)
    qty = fields.Integer(string="Cantidad")

    doff_higiene_seguridad_id = fields.Many2one("doff.higiene.seguridad","doff_higiene_seguridad_id")

#Herencia
class products(models.Model):
    _inherit = "product.product"

    product_higiene_seguridad_check = fields.Boolean("Higiene y seguridad", domain="[('product_higiene_seguridad_check','=',True)]")    