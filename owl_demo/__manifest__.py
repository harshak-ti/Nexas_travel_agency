
{
    'name': 'OWL Demo',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A simple Odoo module with an OWL component',
    'depends': ['web'],
    'data':[
        'security/ir.model.access.csv',
        # 'views/todo_template.xml',
        ],
    'assets': {

        'web.assets_backend':[
            # "owl_demo/static/src/js/components/TodoList.js",
            'owl_demo/static/src/js/main.js'
        ]
   
    },
    'license': 'LGPL-3',
}
