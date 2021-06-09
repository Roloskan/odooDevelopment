# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Generar contratos',
    'version' : '1.0',
    'summary': 'Este modulo es para higiene y seguridad',
    'description': """
    Una peque descripcion
    """,    
    'author': "ICT",
    'category': 'Accounting',
    'website': 'www.roloskan.com',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base','product','stock'],
    'data': [
        'report/doff_contract_report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
