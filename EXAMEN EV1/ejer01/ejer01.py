# definir clase ProductoSimple
class ProductoSimple:
    # definir atributos
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = float(precio)
        # creación de atributo privado
        self.__stock = 10
    
    # definir método mostrar    
    def mostrar(self):
        print(f"Producto: {self.nombre} ({self.precio}€)")
    
    # definir método getter de stock
    @property
    def stock(self):
        return self.__stock
    
    # definir método vender unidades
    def vender(self, unidades):
        if unidades <= self.__stock:
            self.__stock -= unidades
        else: print("No hay suficiente stock.")

# instancias de productos   
p1 = ProductoSimple("Vino", 3)
p2 = ProductoSimple("Cerveza", 1.5)

# mostrar productos
print("\nMOSTRAR PRODUCTOS")
p1.mostrar()     
p2.mostrar()

# comprobar método vender unidades
print("\nVENDER UNIDADES")
print(f"Stock inicial de vino:", p1.stock)
p1.vender(3)
print(f"Stock al vender 3:", p1.stock)

print(f"\nStock inicial de cerveza:", p2.stock)
p2.vender(15)
print(f"Stock al vender 15:", p2.stock)