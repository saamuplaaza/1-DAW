class Libro:
    """Esta clase representa un libro"""
    def __init__(self, isbn, titulo, autor, tipo):
        """Inicializa los atributos de la clase.

        Args:
            isbn (int): El ISBN del libro.
            titulo (str): El título del libro.
            autor (str): El nombre del autor del libro.
            tipo (str): El género del libro.
        """
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.tipo = tipo
        
    def set_isbn(self, isbn):
        self.isbn = isbn
        return self.isbn
    
    def set_titulo(self, titulo):
        self.titulo = titulo
        return self.titulo
    
    def set_autor(self, autor):
        self.autor = autor
        return self.autor
    
    def set_tipo(self, tipo):
        self.tipo = tipo
        return self.tipo
    
    def get_isbn(self):
        return self.isbn
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_tipo(self):
        return self.tipo