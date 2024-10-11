import Libros

class libro:
    def __init__(self, titulo, autor, isbn, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.cantidad = cantidad

# Sobrescritura del metodo __repr__ (Polimorfismo)
    def __repr__(self) -> str:
         #Polimorfismo: redefinimos la forma en que el objeto se representa en texto 
         return f"{self.titulo} por {self.autor_nombre} (ISBN: [{self.isbn}, Disponible: {self.cantidad})"
    