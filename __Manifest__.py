# -*- coding: urf-8 -*-
{
    "name": "Baptiste-Raymond projet",
    'summary': "This is my summary",
    "version": "1.0.0",
    'depends': ['base'],
    'author': "Baptiste Raymond",
    'category': 'Inventory',
    'description': "Module projet odoo",
    
    'data': [
        '__init.py',
        'view/class_view.xml',
        'view/course_view.xml',
        'view/shedule_view.xml',
        'view/student_view.xml',
        'view/res_partner_view.xml',
        'view/menu_view.xml',
        ],
    
    'qweb': [
        'static/src/xml/kanban.xml',
        ],
    
    'demo': ['demo/demo_data.xml',
             ],
    'auto_install': False,
    'installable': True,
    }
    
    


}