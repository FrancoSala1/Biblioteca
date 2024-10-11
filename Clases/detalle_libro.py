import Libros

# Clase Detallelibro hereda de Libros (Herencia)
class DetalleLibro(Libros):
    # Constructor de la clase Detallelibro
    def __init__(self, id_detalle_libro, isbn, fecha_edicion, id_editorial, numero_paginas, id_categoria_libro, cantidad_ejemplares, ejemplares_disponibles):
        Libros.__init__(isbn) #Llamada al constructor de la clase padre (Herencia)
        id_editorial.__init__(id_editorial)
        self.id_detalle_libro = id_detalle_libro
        self.fecha_edicion = fecha_edicion
        self.numero_paginas = numero_paginas
        self.id_categoria_libro = id_categoria_libro
        self.cantidad_ejemplares = cantidad_ejemplares
        self.ejemplares_disponibles = ejemplares_disponibles

# Metodo para actualizar la cantidad de ejemplares disponibles (Encapsulamiento)
    def actualizar_disponibles(self, origen, cantidad):
        if(self.cantidad_ejemplares > self.ejemplares_disponibles + cantidad):
            if(origen == "retirar"):
                if(self.ejemplares_disponibles > 0):
                    self.ejemplares_disponibles = self.ejemplares_disponibles - cantidad
                else:
                    print("No hay ejemplares disponibles para poder hacer el prestamo.")
            else:
                self.ejemplares_disponibles = self.ejemplares_disponibles + cantidad
        else:
            print("Nuestro registro indica que hay error en la cantidad de ejemplares.")