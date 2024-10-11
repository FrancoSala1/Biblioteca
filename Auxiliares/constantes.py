from datetime import datetime

# Estado del usuario (Encapsulamiento)
estado_usuario = {
    "id": 1, "estado": "Habilidato",
    "id": 2, "estado": "Desabilitado"
}

dias_prestamo = 5

# Dias festivos del año actual (Encapsulamiento)
festivos = {
    datetime(datetime.now().year, 1, 1),
    datetime(datetime.now().year, 4, 8),
    datetime(datetime.now().year, 5, 1),
    datetime(datetime.now().year, 5, 21),
    datetime(datetime.now().year, 6, 26),
    datetime(datetime.now().year, 7, 16),
    datetime(datetime.now().year, 8, 15),
    datetime(datetime.now().year, 9, 18),
    datetime(datetime.now().year, 9, 19),
    datetime(datetime.now().year, 10, 12),
    datetime(datetime.now().year, 10, 31),
    datetime(datetime.now().year, 11, 1),
    datetime(datetime.now().year, 12, 8),
    datetime(datetime.now().year, 12, 25),
}