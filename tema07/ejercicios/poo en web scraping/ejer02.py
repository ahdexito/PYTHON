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
    
biblioteca = [
    Book("Don Quijote", "25€", "Sí", "https://ejemplo.com/quijote"),
    Book("La Metamorfosis", "12€", "No", "https://ejemplo.com/kafka"),
    Book("Rayuela", "18.50€", "Sí", "https://ejemplo.com/cortazar"),
    Book("Ficciones", "20", "No", "https://ejemplo.com/borges")
]

print("LIBROS DISPONIBLES")
for libro in biblioteca:
    if libro.is_available():
        print(libro)