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

    'depends': ['base'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'images': ['static/description/icon.png'],
}