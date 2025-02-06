from odoo import models, fields, api



class TiendaCalculos(models.Model):
    _name = 'tienda_calculos'
    _description = 'Cálculos Automáticos para la Tienda'

    name = fields.Char(string='Nombre del Registro', required=True)
    mueble_id = fields.Many2one('tienda_muebles', string='Mueble')
    precio_unitario = fields.Float(
        string='Precio Unitario', 
        related='mueble_id.price', 
        store=True
    )   
    cantidad = fields.Integer(string='Cantidad', required=True)
    precio_unitario = fields.Float(string='Precio Unitario', related='mueble_id.price', store=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)
    descuento = fields.Float(string='Descuento (%)', default=0.0)
    total_con_descuento = fields.Float(string='Total con Descuento', compute='_compute_total_con_descuento', store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_unitario

    @api.depends('subtotal', 'descuento')
    def _compute_total_con_descuento(self):
        for record in self:
            record.total_con_descuento = record.subtotal * (1 - record.descuento / 100)


