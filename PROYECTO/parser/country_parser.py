from bs4 import BeautifulSoup
import re

class CountryParser:
    
    @staticmethod
    def parse_countries(html: str) -> list:
        """
        Extraer los países de la tabla y del HTML de 
        Worldmeter y devolver una lista de diccionarios.
        """
        
        soup = BeautifulSoup(html, "html.parser")
        countries = []
        
        # Buscar la tabla de países
        table = soup.select_one("table")
        if not table:
            raise Exception("No se encontró la tabla de países")
        
        rows = table.select("tbody tr")

        for row in rows:
            cols = row.find_all("td")
            
            if len(cols) < 6:
                continue
            
            name = cols[1].text.strip()
            
            # Limpiar números con regex, quitar comas
            raw_population = cols[2].text.strip()
            population = re.sub(r"[^\d]", "", raw_population)
            population = int(population) if population else None
            
            raw_density = cols[5].text.strip()
            density = re.sub(r"[^\d]", "", raw_density)
            density = int(density) if density else None

            if name and population:
                countries.append({
                    "name": name,
                    "population": population,
                    "density": density
                })
                
        return countries