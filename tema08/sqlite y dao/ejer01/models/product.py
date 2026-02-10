class Product:
    def __init__(self, nombre, precio, stock, url):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.url = url
        
    def __str__(self):
        return f"[{self.stocl}] {self.nombre} - {self.precio}"