{
    'name': "Reserva de salas",
    'version': '1.0',
    'depends': ['base'],
    'author': "Mantenimiento Informático",
    'category': 'Services',
    'description': """
    Módulo para la reserva de aulas y espacios del centro
    """,
    'data': [
        'security/ir.model.access.csv',
        'security/booking_room_security.xml',
        'views/booking_room_views.xml',
        'views/room_views.xml',
        'views/booking_room_menus.xml'
    ]
}