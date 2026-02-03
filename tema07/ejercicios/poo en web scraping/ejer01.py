class Book:
    def __init__(self, titulo, precio, disponible, url):
        self.titulo = titulo
        self.precio = precio
        self.disponible = disponible
        self.url = url

libro1 = Book("El Alquimista", "15.50€", True, "https://ejemplo.com/alquimista")
libro2 = Book("Cien Años de Soledad", "22€", False, "https://ejemplo.com/soledad")

print("CONSULTA DE LIBROS")

print(f"Libro 1: {libro1.titulo}")
print(f"Precio: {libro1.precio}")
print(f"Disponible: {libro1.disponible}")
print(f"Enlace: {libro1.url}")

print()

print(f"Libro 2: {libro2.titulo}")
print(f"Precio: {libro2.precio}")
print(f"Disponible: {libro2.disponible}")
print(f"Enlace: {libro2.url}")