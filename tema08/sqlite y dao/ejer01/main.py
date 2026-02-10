from models.product import Product
from dao.product_dao import ProductDAO

productos_raw = [
    {"nombre": "Laptop", "precio": "1200€", "stock": "Sí", "url": "http://tienda.com/laptop"},
    {"nombre": "Cámara", "precio": "850€", "stock": "No", "url": "http://tienda.com/camara"},
    {"nombre": "Auriculares", "precio": "150€", "stock": "Sí", "url": "http://tienda.com/audio"},
    {"nombre": "Smartphone", "precio": "900€", "stock": "No", "url": "http://tienda.com/movil"},
    {"nombre": "Cable HDMI", "precio": "8€", "stock": "No", "url": "http://tienda.com/cablehdmi"},
    {"nombre": "Monitor", "precio": "300€", "stock": "Sí", "url": "http://tienda.com/monitor"},
    {"nombre": "Smartwatch", "precio": "130€", "stock": "Sí", "url": "http://tienda.com/smartwatch"},
    {"nombre": "Ratón", "precio": "25€", "stock": "Sí", "url": "http://tienda.com/raton"},
    {"nombre": "Teclado", "precio": "20€", "stock": "Sí", "url": "http://tienda.com/teclado"},
    {"nombre": "Alfombrilla", "precio": "12€", "stock": "No", "url": "http://tienda.com/alfombrilla"}
]

lista_productos = [Product(**data) for data in productos_raw]

dao = ProductDAO()

dao.delete_all()

dao.bulk_insert(lista_productos)

print("# TODOS LOS PRODUCTOS #")
for p in dao.select_all():
    print(p)

print()

print("# PRODUCTOS EN STOCK #")
for p in dao.select_in_stock():
    print(p)