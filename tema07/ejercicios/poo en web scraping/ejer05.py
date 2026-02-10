class Product:
    def __init__(self, nombre, precio, stock, url):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.url = url

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or not value.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = value
        
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"

    def is_in_stock(self):
        if isinstance(self.stock, bool):
            return self.stock

        return str(self.stock).lower() in ["si", "sí", "disponible", "yes", "in stock"]

products_data = [
    {"nombre": "Teclado", "precio": "85.00€", "stock": "Sí", "url": "https://tienda.com/teclado"},
    {"nombre": "Ratón", "precio": "45.00€", "stock": "No", "url": "https://tienda.com/raton"},
    {"nombre": "Monitor", "precio": "320.00€", "stock": "Sí", "url": "https://tienda.com/monitor"},
    {"nombre": "Alfombrilla", "precio": "15.00€", "stock": "No", "url": "https://tienda.com/alfombrilla"}
]

inventory = [Product(**data) for data in products_data]

print("PRODUCTOS DISPONIBLES")
for product in inventory:
    if product.is_in_stock():
        print(product)