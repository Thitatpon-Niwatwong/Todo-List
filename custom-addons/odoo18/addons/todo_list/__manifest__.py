{
    'name': 'Todo List Manager',
    'version': '1.0',
    'depends': ['base', 'web'],
    'author': 'Your Name',
    'category': 'Productivity',
    'description': 'Manage internal todo lists with full CRUD and tracking',
    'data': [
        'security/security.xml',
        'views/todo_list_views.xml',
        'security/ir.model.access.csv',
        'data/todo_tag_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'todo_list/static/src/css/todo_list_styles.css',
        ],
    },
    'installable': True,
    'application': True,
}
