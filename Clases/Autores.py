from datetime import datetime
import Paises
#La clase Autor de la clase Paises (Herencia)
class Autor(Paises):
    #Constructor de la clase Autor
    def __init__(self, id_autor, nombre_autor, codigo_pais, fecha_nac, fecha_def, biografia_autor, foto_autor):
        super()._init_(codigo_pais)
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.fecha_nac = fecha_nac
        self.fecha_def = fecha_def
        self.biografia_autor = biografia_autor
        self.foto_autor = foto_autor

#Metodo para formatear una fecha (Encapsulamiento)
    def fechas(fecha):
        fecha_dt = datetime.strptime(fecha, '%d/%m/%y')
        fecha_str = fecha_dt.strftime('%Y-%m-%d')
        return fecha_str
    #Metodo para agregar libros al Autor (encapsulamiento)
    def agregar_libro(self, libro):
        self.libros.append(libro) #Encapsula la funcionalidad de agregar libros a la lista de libros de autor
