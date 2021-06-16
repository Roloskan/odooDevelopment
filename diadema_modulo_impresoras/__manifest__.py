# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Modulo de impresoras',
    'version' : '1.0',
    'summary': 'Conocer y controlar el consumo por departamento.',
    'sequence': 30,
    'description': """
    Este modulo fue hecho con amor.
    """,    
    'author': "ICT",
    'category': 'Accounting',
    'depends' : ['base'],
    'data': [
        'wizard/printer_report_between_two_dates.xml',
        'wizard/anual_report.xml',
        'report/report_printer_by_month.xml',    
        'security/security.xml',
        'security/ir.model.access.csv',    
        'views/printer.xml',
        'views/device.xml',
        'views/department.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
