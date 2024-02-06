# -*- coding: utf-8 -*-
{
    'name': "Módulo de Prueba",

    'summary': "Módulo de prueba para el entrenamiento de Soutec",

    'description': "Soutec está aprendiendo a programar en Odoo",

    'author': "Profesora Monica Tahan",
    'website': "http://www.soutec-group.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Other',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vista_prueba.xml',
        'views/service_detail.xml',
        'views/main_menu_file.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    "license":'OPL-1',
}
