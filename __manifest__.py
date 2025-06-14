{
    'name': 'Quiz Engine Ultra',
    'summary': 'Advanced Quiz Engine for Odoo 17 CE',
    'description': '''
        A modular, high-performance quiz engine built for education platforms, 
        mock test apps, and certification systems.
        Features include custom question types, adaptive quizzes, detailed analytics,
        PDF reports, and a sleek frontend UI.
    ''',
    'version': '17.0.1.0.0',
    'category': 'Education',
    'author': 'Odoocrafts',
    'website': 'https://github.com/yourorg/quiz_engine_ultra',
    'license': 'MIT',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/quiz_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
}
