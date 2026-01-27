import re

texto = """
Nombre: Juan Pérez
Correo: juan.perez@example.com
Precio: 199.99 EUR
Código cliente: ABC-12345
"""

# limpiar espacios
texto_limpio = re.sub(r"\s+", " ", texto).strip()

# extraer correo electrónico
correo = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto_limpio)
correo = correo.group() if correo else None

# extraer precio y convertir float
precio = re.search(r"Precio:\s*([0-9]+\.[0-9]+)", texto_limpio)
precio = float(precio.group(1)) if precio else None

# extraer código de cliente
codigo = re.search(r"[A-Z]{3}-\d{5}", texto_limpio)
codigo = codigo.group() if codigo else None

# mostrar resultados
print("Texto limpio:", texto_limpio)
print("Correo:", correo)
print("Precio:", precio)
print("Código cliente:", codigo)


# EXTRA
# extraer palabras que empiezan por mayúscula
nombre_propios = re.findall(r"[A-Z][a-z]+", texto_limpio)

print(nombre_propios)