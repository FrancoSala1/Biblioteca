import Libros

class libro:
    def __init__(self, titulo, autor, isbn, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.cantidad = cantidad

    def __repr__(self) -> str:
         return f"{self.titulo} por {self.autor_nombre} (ISBN: [{self.isbn}, Disponible: {self.cantidad})"
    