import json

# definir clase Producto
class Producto:
    # definir atributos
    def __init__(self, id, nombre, categoria, precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
    
    # método para cargar cada objeto a json como diccionario
    def to_dict(self):
        return {"id":self.id,"nombre":self.nombre,"categoria":self.categoria,"precio":self.precio}
    
    # método para imprimir como string el objeto   
    def __str__(self):
        return f"Producto: {self.nombre} ({self.precio}€) - Categoría: {self.categoria}"

# leer fichero json y almacenar datos
with open("productos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)  

# crear lista de objetos reconstruidos
productos = [
    Producto(
        d["id"], 
        d["nombre"], 
        d["categoria"], 
        d["precio"])
    for d in datos]

# mostrar todos los productos con formato
print("\nLISTA COMPLETA DE PRODUCTOS")
for p in productos:
    print(p)
    
# filtrar productos destacados
productos_destacados = []
for p in productos:
    if float(p.precio) > 100:
        productos_destacados.append(p)
        
# mostrar productos destacados
print("\nLISTA DE PRODUCTOS CON PRECIO MAYOR A 100€")
for p in productos_destacados:
    print(p)
    
# guardar productos filtrados en json
with open("productos_destacados.json", "w", encoding="utf-8") as f:
    json.dump([p.to_dict() for p in productos_destacados], f, indent=4)