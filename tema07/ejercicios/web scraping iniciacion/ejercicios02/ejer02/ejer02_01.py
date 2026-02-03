from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
    <a href="https://example.com" class="btn enlace">Visitar</a>
    <img src="img/logo.png" alt="Logo principal" id="logo">
    <div id="info">
        <p>Teléfono: <span>+34 123 456 789</span></p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# extraer texto del enlace
enlace = soup.select_one(".enlace")

# obtener datos
texto_enlace = enlace.get_text()
url = enlace['href']
lista_clases = enlace['class']

# imprimir datos
print(f"Texto del enlace: {texto_enlace}")
print(f"URL: {url}")
print(f"Lista de clases: {lista_clases}")

# extraer src de imagen
imagen_src = soup.select_one("#logo")['src']
print(f"SRC de imagen: {imagen_src}")

# obtener teléfono
telefono = soup.select_one("#info span").text
print(f"Contacto: {telefono}")


# EXTRA
# unir lista de clases separadas por comas
clases_string = ", ".join(lista_clases)
print(f"Clases String: {clases_string}")