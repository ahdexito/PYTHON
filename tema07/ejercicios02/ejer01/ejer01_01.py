from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>Mi Página de Prueba</title></head>
<body>
    <div id="contenedor">
        <h1>Bienvenido</h1>
        <p class="intro">Este es un párrafo introductorio.</p>
        <p class="intro destacado">Este párrafo tiene dos clases.</p>
        <div class="articulo">
            <h2>Título del artículo</h2>
            <p>Contenido del artículo...</p>
        </div>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# extraer el título
titulo = soup.select_one('title')

# obtener elementos
parrafos_intro = soup.select('p.intro')
h2_articulo = soup.select('.articulo h2')

# mostrar el texto de cada uno
print(f"--- Título de la página ---")
print(titulo.get_text())

print(f"\n--- Párrafos con clase .intro ---")
for p in parrafos_intro:
    print(f"- {p.get_text()}")

print(f"\n--- h2 dentro de .articulo ---")
for h2 in h2_articulo:
    print(f"- {h2.get_text()}")


# EXTRA    
# seleccionar el segundo párrafo
intro_destacado = soup.select('.intro.destacado')[0].get_text()
print(f"\n--- Intro destacado ---")
print(intro_destacado)