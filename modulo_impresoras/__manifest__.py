# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Modulo de impresoras',
    'version' : '1.0',
    'summary': 'Este es mi primer modulo en Odoo 11',
    'sequence': 30,
    'description': """
    Este modulo fue hecho con amor.
    """,    
    'author': "ICT",
    'category': 'Accounting',
    'website': 'www.roloskan.com',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base'],
    'data': [
        'report/report_anual.xml',
        'report/report_printer.xml',
        'report/report.xml',
        'security/security.xml',
        'views/printer.xml',
        'views/device.xml',
        'views/department.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
