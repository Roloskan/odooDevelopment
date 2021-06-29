# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Calendario de Reuniones',
    'version' : '1.0',
    'summary': 'Programacion de reuniones.',
    'description': """
    Una peque descripcion
    """,    
    'author': "ICT",
    'category': '',
    'website': '',
    'images' : ['static/description/icon.png'],
    'depends' : ['base','hr'],
    'data': [
        'views/meeting_schedule.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
