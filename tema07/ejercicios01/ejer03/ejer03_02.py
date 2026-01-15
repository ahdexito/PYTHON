import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.worldometers.info/coronavirus/"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")

    tabla = soup.find("table", id="main_table_countries_today")
    filas = tabla.tbody.find_all("tr")
    
    datos = []
    
    for fila in filas:
        columnas = fila.find_all("td")
        if columnas:
            pais = columnas[1].text.strip()
            casos = columnas[2].text.strip()
            muertes = columnas[4].text.strip()
            recuperados = columnas[6].text.strip()
            
            datos.append([pais, casos, muertes, recuperados])
            
    print(f"{'País':25} {'Casos':15} {'Muertes':15} {'Recuperados':15}")
    print("-" * 70)
    
    for d in datos:
        print(f"{d[0]:25} {d[1]:15} {d[2]:15} {d[3]:15}")
        
    with open("covid_paises.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["País", "Casos", "Muertes", "Recuperados"])
        writer.writerows(datos)
    
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la página o procesar: {e}")