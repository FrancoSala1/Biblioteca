from datetime import datetime, timedelta
from Auxiliares import constantes
import Clases.Detalle_libro as detalle_libro
import Usuario 

#Clase prestamo que gestiona los prestamos de libros
class prestamo:
    #Constructor de prestamo
    def __init__(self, id_prestamo, isbn, id_usuario, fecha_prestamo, fecha_devolucion, fecha_devuelto, cantidad_solicitada):
        detalle_libro.__init__(isbn) # Herencia: Llamada al constructor de la clase Detalle_libro
        Usuario.__init__(id_usuario) # Herencia: Llamada al constructor de la clase Usuario
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = id.prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_devuelto
        self.cantidad_solicitada = cantidad_solicitada

# Metodo para sumar dias laborales a la fecha de prestamo
    def sumas_dias_laborales(fecha_prestamo, dias_prestamo):
        dias_agregados = 0
        while dias_agregados < dias_prestamo:
            fecha_prestamo += timedelta(dias=1)
            if fecha_prestamo.weekday() < 5 and fecha_prestamo not in constantes.festivos:
                dias_agregados += 1
        return fecha_prestamo
    
    # Metodo para calcular las fechas de prestamo
    def calcular_fechas(self):
        if(self.ejemplares_disponibles > 0):
            if(self.ejemplares_disponibles > self.cantidad_solicitada):
                self.fecha_prestamo = datetime.datetime.now() # Aqui se utiliza (Encapsulamiento)
                self.fecha_devolucion = prestamo.sumas_dias_laborales(self.fecha_prestamo, 5)

     