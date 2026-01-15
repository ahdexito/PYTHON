import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    noticias = soup.find_all('span', class_='titleline')
    
    resultado = []
    
    for noticia in noticias:
        enlace = noticia.find('a')
        titulo = enlace.text
        link = enlace["href"]
        
        if "Python" in titulo:
            resultado.append({
                "title": titulo,
                "link": link
            })
        
    for n in resultado:
        print(n)
    
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la página o procesar: {e}")