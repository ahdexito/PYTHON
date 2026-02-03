from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
    <div class="noticias">
        <article class="post destacado">
            <h2>Economía en crecimiento</h2>
            <p class="autor">Por Ana López</p>
            <p class="contenido">El PIB aumentó un 3% durante el último trimestre.</p>
        </article>
        <article class="post">
            <h2>Nuevo descubrimiento científico</h2>
            <p class="autor">Por Dr. Martín Pérez</p>
            <p class="contenido">Se encontró una nueva partícula subatómica.</p>
        </article>
        <article class="post destacado">
            <h2>Innovación en IA</h2>
            <p class="autor">Por Carla Ruiz</p>
            <p class="contenido">La nueva tecnología revoluciona el sector.</p>
        </article>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# seleccionar .post.destacado y mostrar datos
print("--- ARTÍCULOS DESTACADOS ---")
destacados = soup.select(".post.destacado")

for post in destacados:
    titulo = post.select_one("h2").get_text()
    autor = post.select_one(".autor").get_text()
    contenido = post.select_one(".contenido").get_text()

    # calcular 15% del texto
    limite = int(len(contenido) * 0.15)
    preview = contenido[:limite]

    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Preview 15%: {preview}...")
    print("-" * 20)


# EXTRA
# selector avanzado para el segundo h2 dentro de .noticias
segundo_h2 = soup.select(".noticias .post:nth-of-type(2) h2")[0].get_text()

print(f"\nSegundo h2 encontrado: {segundo_h2}")

# obtener todos los títulos ordenados alfabéticamente
# seleccionar todos los h2 dentro de artículos
titulos = soup.select(".post h2")

# extraer texto de cada uno y guardar en lista
lista_titulos = [t.get_text() for t in titulos]

# ordenar lista
titulos_ordenados = sorted(lista_titulos)

# mostrar uno a uno
print(f"\n--- TÍTULOS ORDENADOS ---")
for titulo in titulos_ordenados:
    print(f"* {titulo}")