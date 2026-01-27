import re

texto = """
=== FICHA PERSONAL ===
Nombre completo: María Gómez García
Email de contacto: maria.gomez+work@example.co.uk
Teléfonos: +34-600-123-456 / 600 777 888
Dirección: Calle Falsa nº 123, 3ºB — Madrid (CP: 28080)
Salario anual: 32.500 €
Código interno: EMP-00AB-1299
"""

# normalizar espacios
texto = re.sub(r"\s+", " ", texto).strip()

# extracciones con regex
nombre = re.search(r"Nombre completo:\s([A-Za-zÁÉÍÓÚáéíóúñÑ ]+) Email", texto).group(1)

email = re.search(r"[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto).group()

telefonos = re.findall(r"\+?\d{2,3}[- ]?\d{3}[- ]?\d{3}[- ]?\d{3}", texto)

codigo_postal = re.search(r"\b\d{5}\b", texto).group()

# salario - quitar puntos y convertir a floar
salario = re.search(r"Salario anual:\s([\d.]+)", texto).group(1)
salario = float(salario.replace(".", ""))

codigo_interno = re.search(r"EMP-\d{2}[A-Z]{2}-\d{4}", texto).group()

# diccionario final
datos = {
    "nombre": nombre,
    "email": email,
    "telefonos": telefonos,
    "codigo_postal": codigo_postal,
    "salario": salario,
    "codigo_interno": codigo_interno
}

print(datos)


# EXTRA
ciudad = re.search(r"—\s*([A-Za-zÁÉÍÓÚáéíóúñÑ ]+)\s*\(CP:", texto).group(1)

print(ciudad)