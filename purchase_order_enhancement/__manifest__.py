{
    'name': 'Purchase Order Enhancement',
    'version': '1.0',
    'description': """""",
    'depends': ['purchase'],
    'data': [
        'data/cron.xml',
        'security/ir.model.access.csv',
        'reports/purchase_order_template.xml',
        'reports/purchase_report_views.xml',
        'views/purchase_order_view.xml',
        'views/res_config_settings_views.xml',
        'wizard/archive_purchase_orders_views.xml',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'purchase_order_enhancement/static/src/js/us_phone.js',
        ]
    },
}