import requests
from bs4 import BeautifulSoup

url_base = "https://books.toscrape.com/catalogue/page-1.html"
url = url_base

libros = []
total_5_estrellas = 0

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articulos = soup.find_all("article", class_="product_pod")
    
    for articulo in articulos:
        
        titulo = articulo.h3.a["title"]
        
        precio = articulo.find("p", class_="price_color").text
        
        clase_estrellas = articulo.find("p", class_="star-rating")["class"]
        estrellas = clase_estrellas[1]
        
        libros.append({
            "titulo": titulo,
            "precio": precio,
            "estrellas": estrellas
        })
        
        if estrellas == "Five":
            total_5_estrellas += 1
            
    siguiente = soup.find("li", class_="next")
    if siguiente:
        enlace = siguiente.a["href"]
        url = "https://books.toscrape.com/catalogue/" + enlace
    else:
        url = None
        
print("Total de libros recopilados:", len(libros))
print("Total de libros con 5 estrellas:", total_5_estrellas)