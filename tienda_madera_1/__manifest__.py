{
    'name': 'Tienda de Maderas',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Gestión de una tienda de maderas',
    'author': 'Tu Nombre',
    'website': 'http://www.tutienda.com',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/maderas_views.xml',
    ],
    'installable': True,
    'application': True,
}