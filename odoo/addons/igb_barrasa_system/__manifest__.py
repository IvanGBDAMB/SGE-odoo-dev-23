# -*- coding: utf-8 -*-
{
    'name': "Barrasa System",

    'summary': "Módulo para registrar la actividad de usuarios en cualquier web mediante código JavaScript",

    'description': """
Barrasa System permite añadir un código JavaScript a cualquier sitio web para registrar la actividad de los usuarios.
Luego, estos datos pueden vincularse con clientes dentro de Odoo, proporcionando un seguimiento detallado de su interacción.
    """,

    'author': "Ivan Gonzalez Barrasa",
    'website': "https://barrasa.dev",

    'category': 'Marketing',
    'version': '17.0.1.0',
    'license': 'LGPL-3',

    'depends': ['base', 'web'],

    'data': [
        'security/igb_barrasa_system_security.xml',
        'security/ir.model.access.csv',
        'views/campana_views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'images': ['static/description/icon.png'],

    'assets': {
        'web.assets_backend': [
            'igb_barrasa_system/static/src/js/modal_personalizado.js',
        ],
    },


}