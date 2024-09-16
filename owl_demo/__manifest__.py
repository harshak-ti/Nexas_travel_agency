
{
    'name': 'OWL Demo',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A simple Odoo module with an OWL component',
    'depends': ['web'],
    'data':[
        'security/ir.model.access.csv',
        'views/sample_view.xml',
        'views/menus.xml'
        ],
    'assets': {

        'web.assets_backend':[
            'owl_demo/static/src/js/Counter.js',
            'owl_demo/static/src/js/main.js'
        ]
   
    },
    'license': 'LGPL-3',
}
