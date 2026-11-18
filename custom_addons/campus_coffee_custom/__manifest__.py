{
    'name': 'Campus Coffee & Tea - Custom Theme',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Custom coffee-brown theme for Campus Coffee POS',
    'depends': ['point_of_sale', 'web'],
    'data': [],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'campus_coffee_custom/static/src/scss/theme_coffee.scss'),
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}