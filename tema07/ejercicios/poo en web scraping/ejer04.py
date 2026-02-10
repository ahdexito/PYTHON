class Book:
    def __init__(self, titulo, precio, disponible, url):
        self._titulo = titulo
        self.precio = precio
        self.disponible = disponible
        self.url = url
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if not value or not value.strip():
            raise ValueError("El título no puede estar vacío.")
        self._titulo = value
        
    def __str__(self):
        return f"- {self.titulo} | Precio: {self.precio} | Disponible: {self.disponible}"

    def is_available(self):
        return self.disponible.lower() in ["sí", "si", "available", "yes"]
    
try:
    libro = Book("Crónica de una muerte anunciada", 19.99, "Sí", "https://ejemplo.com/cronica")
    print("Objeto creado con éxito:")
    print(libro)
    
    print("\nAsignación de título vacío...")
    libro.titulo = "" 
    
except ValueError as e:
    print(f"ERROR: {e}")