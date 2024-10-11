
{
    'name': 'OWL Demo',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A simple Odoo module with an OWL component',
    'depends': ['web'],
    'data':[
        'security/ir.model.access.csv',
        'views/todo_template.xml',
        "views/menus.xml"
        ],
    'assets': {

        'web.assets_backend':[
            # "owl_demo/static/src/js/components/TodoList.js",
            "owl_demo/static/src/js/field_widget.scss",
            'owl_demo/static/src/js/main.js',
            'owl_demo/static/src/js/main.xml',
            "owl_demo/static/src/js/selection_field.scss",
            'owl_demo/static/src/js/selection_field_widget.js',
            'owl_demo/static/src/js/selection_field_options.xml'
        ]
   
    },
    'license': 'LGPL-3',
}
