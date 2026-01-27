from bs4 import BeautifulSoup

html = """
<div class="alumno">
    <h3>Laura Gómez</h3>
    <span class="nota"> 8.5 </span>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

def parsear_alumno(soup):
    nombre = soup.find("h3").text.strip()
    nota = float(soup.find("span", class_="nota").text.strip())
    return nombre, nota

resultado = parsear_alumno(soup)
print(resultado)