{
    'name': 'Campus Coffee & Tea - Custom Theme & F&B Operations',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Tuy chinh giao dien thuong hieu Ca phe & mo rong nghiep vu pha che POS',
    'depends': ['point_of_sale', 'web'],
    'data': [
        'views/pos_order_views.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'campus_coffee_custom/static/src/scss/theme_coffee.scss'),
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}