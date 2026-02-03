from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
    <ul id="catalogo">
        <li class="producto" data-id="A123" data-stock="25">
            <span class="nombre">Teclado Mecánico</span>
            <span class="precio">79.99€</span>
        </li>
        <li class="producto agotado" data-id="B450" data-stock="0">
            <span class="nombre">Monitor 27"</span>
            <span class="precio">229.50€</span>
        </li>
        <li class="producto" data-id="C777">
            <span class="nombre">Ratón inalámbrico</span>
            <span class="precio">34.95€</span>
        </li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# extraer todos los .producto
productos = soup.select(".producto")
lista_productos = []

# procesar cada producto
for p in productos:
    # extraer datos
    p_id = p['data-id']
    nombre = p.select_one(".nombre").get_text()
    
    # limpieza de precio
    precio_limpio = p.select_one(".precio").get_text()
    precio_float = float(precio_limpio.replace('€', '').replace(',', '.').strip())

    # manejo de stock
    stock_atrib = p.get('data-stock')
    if stock_atrib is None or stock_atrib == "":
        stock = "Sin dato"
    else:
        stock = int(stock_atrib)

    # crear diccionario
    item = {
        "id": p_id,
        "nombre": nombre,
        "precio": precio_float,
        "stock": stock
    }
    lista_productos.append(item)

# mostrar productos con stock
print("--- PRODUCTOS CON STOCK DISPONIBLE ---")
for prod in lista_productos:
    # verificar si es entero y mayor que 0
    if isinstance(prod['stock'], int) and prod['stock'] > 0:
        print(f"ID: {prod['id']} | {prod['nombre']} - {prod['precio']}€ (Stock: {prod['stock']})")


# EXTRA
# generar diccionario
diccionario_precios = {
    p['data-id']: float(p.select_one(".precio").get_text().replace('€', '').replace(',', '.').strip())
    for p in productos
}

# mostrar resultado
print(diccionario_precios)