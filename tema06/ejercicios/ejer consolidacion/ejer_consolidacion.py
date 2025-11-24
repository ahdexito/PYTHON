import json
import csv
import os

class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        
    # convertir objeto a diccionario
    def to_dict(self):
        return {"nombre":self.nombre,"categoria":self.categoria,"precio":self.precio,"stock":self.stock}
    
    # convertir objeto a string
    def __str__(self):
        return f"* Nombre: {self.nombre}; Categoría: {self.categoria}; Precio: {self.precio}; Stock: {self.stock}"

# cargar productos desde cada json
datos_total = []
for archivo in os.listdir():
    if archivo.endswith(".json"):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            datos_total.extend(datos)

# combinar productos en una lista
productos = [
    # reconstruir objetos
    Producto(d["nombre"], d["categoria"], d["precio"], d["stock"]) 
    for d in datos_total
]

# mostrar todos los productos
print("\nLISTA GENERAL DE PRODUCTOS")
for producto in productos:
    print(producto)
    
# filtrar productos
productos_filtrados = []
for producto in productos:
    if producto.precio >= 50 and producto.stock >= 10:
        productos_filtrados.append(producto)
        
# mostrar productos filtrados
print("\nPRODUCTOS FILTRADOS")
for producto in productos_filtrados:
    print(producto)
    
# calcular precio medio
media = sum(p.precio for p in productos) / len(productos)

# imprimir media
print("\nPRECIO MEDIO DEL TOTAL DE PRODUCTOS")
print("*", round(media, 2))

# crear nuevo json con productos filtrados
with open("productos_destacados.json", "w", encoding="utf-8") as f:
    json.dump([producto.to_dict() for producto in productos], f, indent=4)
    
# exportar productos a csv
with open("todos_productos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Categoría", "Precio", "Stock"])
    for producto in productos:
        writer.writerow([
            producto.nombre,
            producto.categoria,
            producto.precio,
            producto.stock
        ])