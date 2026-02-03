import re

usuario = {
    "nombre": "Laura",
    "edad": "21",
    "email": "laura@gmail.com",
    "precio": "199.99"
}

valido = True

# validar nombre
if not usuario["nombre"].strip():
    valido = False

# validar edad
if usuario["edad"].isdigit() and int(usuario["edad"]) > 0:
    usuario["edad"] = int(usuario["edad"])
else:
    valido = False

# validar email
if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", usuario["email"]):
    valido = False

# validar precio
try:
    precio = float(usuario["precio"])
    if precio > 0:
        usuario["precio"] = precio
    else:
        valido = False
except:
    valido = False

# resultado final
if valido:
    print("Usuario válido")
    print(usuario)
else:
    print("Usuario no válido")