from bs4 import BeautifulSoup

html = """
<ul>
    <li class="producto">Teclado - 19.99 €</li>
    <li class="producto">Ratón - 12.50 €</li>
    <li class="producto">Monitor - 179.00 €</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")

def parsear_productos(soup):
    productos = []
    items = soup.find_all("li", class_="producto")

    for item in items:
        texto = item.text.strip()
        nombre, precio = texto.split("-")

        nombre = nombre.strip()
        precio = precio.replace("€", "").strip()
        precio = float(precio)

        productos.append((nombre, precio))

    return productos

resultado = parsear_productos(soup)
print(resultado)