{
    'name': 'Purchase Order Enhancement',
    'version': '1.0',
    'description': """""",
    'depends': ['purchase'],
    'data': [
        'data/cron.xml',
        'security/ir.model.access.csv',
        'wizard/archive_purchase_orders_views.xml',
        'views/purchase_order_view.xml',
    ],
    'demo': [],
}