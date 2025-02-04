from odoo import models, fields

class Madera(models.Model):
    _name = 'tienda.madera'
    _description = 'Madera'

    name = fields.Char(string='Nombre', required=True)
    densidad = fields.Float(string='Densidad (g/cm2)', default=0.0, help="Densidad en (g/cm2)")
    description = fields.Text(string='Descripción') 
    fecha_tala = fields.Char(string='Fecha de tala')
    
    madera_type = fields.Selection(
        [('madera', 'Madera'),
         ('nogal', 'Nogal'),
         ('pino', 'Pino'),
         ('acacia', 'Acacia')],
        string='Árbol de origen',
        required=True,
        default='madera'
    )

    brand = fields.Text(string='Descripción', help="Descripción del producto.")
    category_id = fields.Many2one('tienda.madera.categoria', string='Categoría')

    dureza_type = fields.Selection(
        [('blando', 'Blando'),
         ('poco_blando', 'Muy blando'),
         ('normal', 'Normal'),
         ('duro', 'Duro'),
         ('muy_duro', 'Muy duro')],
        string='Dureza',
        required=True,
        default='blando'
    )

    barniz_type = fields.Selection(
        [('si', 'Sí'),
         ('no', 'No')],
        string='Barniz',
        required=True,
        default='si'
    )

    # Campo de relación con Empleados
    empleado_id = fields.Many2one('hr.employee', string='Empleado Responsable')

class MaderaCategoria(models.Model):
    _name = 'tienda.madera.categoria'
    _description = 'Categoría de Maderas'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    madera_ids = fields.One2many('tienda.madera', 'category_id', string='Maderas')
