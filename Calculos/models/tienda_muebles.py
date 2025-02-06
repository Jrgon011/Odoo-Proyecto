from odoo import models, fields

class TiendaMuebles(models.Model):
    _name = 'tienda_muebles'
    _description = 'Muebles para Tienda'

    name = fields.Char(string='Nombre del Mueble', required=True)
    price = fields.Float(string='Precio', required=True)
    mueble_id = fields.Many2one('tienda_calculos', string='Cálculo Relacionado')
    precio_unitario = fields.Float(string='Precio Unitario', related='mueble_id.precio_unitario', store=True)


