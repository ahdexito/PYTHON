import re

correos = [
    "ana@gmail.com",
    "pepe@email",
    "juan@empresa.org",
    "correo@dominio"
]

patron = r"^[\w.-]+@[\w.-]+\.\w+$"

print("Correos válidos:")
for correo in correos:
    if re.match(patron, correo):
        print(correo)

print("\nCorreos inválidos:")
for correo in correos:
    if not re.match(patron, correo):
        print(correo)