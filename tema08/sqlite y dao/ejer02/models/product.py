class Product:
    def __init__(self, nombre, precio, stock, url):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.url = url
        
    def is_in_stock(self):
        return self.stock.lower() in ["sí", "si", "yes"]

    def is_cheap(self):
        try:
            valor_numerico = float(self.precio.replace('€', '').strip())
            return valor_numerico < 30
        except ValueError:  
            return False
        
    def __str__(self):
        return f"[{self.stock}] {self.nombre} - {self.precio}"