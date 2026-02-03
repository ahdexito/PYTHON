class Book:
    def __init__(self, titulo, precio, disponible, url):
        self.titulo = titulo
        self.precio = precio
        self.disponible = disponible
        self.url = url
        
    def __str__(self):
        return f"- {self.titulo} | Precio: {self.precio} | Disponible: {self.disponible}"

    def is_available(self):
        return self.disponible.lower() in ["sí", "si", "available", "yes"]

books_data = [
    {"titulo": "Python Básico", "precio": "18€", "disponible": "Sí", "url": "http://ejemplo.com/1"},
    {"titulo": "Python Avanzado", "precio": "35€", "disponible": "No", "url": "http://ejemplo.com/2"}
]

books = [Book(**data) for data in books_data]

print("LIBROS CREADOS")
for book in books:
    print(book)
    
print()
    
print("LIBROS DISPONIBLES")
for book in books:
    if book.is_available():
        print(book)