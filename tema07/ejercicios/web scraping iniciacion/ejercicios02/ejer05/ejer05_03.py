import re

datos = {
    "producto": "Monitor",
    "precio": "abc",
    "stock": "-3",
    "email": "tienda@web"
}

errores = []

# validar precio
try:
    precio = float(datos["precio"])
    if precio <= 0:
        errores.append("El precio debe ser positivo")
except ValueError:
    errores.append("El precio no es numérico")

# validar stock
try:
    stock = int(datos["stock"])
    if stock < 0:
        errores.append("El stock debe ser mayor o igual que 0")
except ValueError:
    errores.append("El stock no es un número entero")

# validar email
patron_email = r"^[\w.-]+@[\w.-]+\.\w+$"
if not re.match(patron_email, datos["email"]):
    errores.append("El email no tiene un formato válido")

# mostrar resultado
if errores:
    print("Errores encontrados:")
    for e in errores:
        print("-", e)
else:
    print("Datos válidos")