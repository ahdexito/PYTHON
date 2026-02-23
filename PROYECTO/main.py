from scraper.scraper_engine import ScraperEngine
from parser.country_parser import CountryParser
from models.country import Country
from dao.country_dao import CountryDAO

URL = "https://www.worldometers.info/world-population/population-by-country/"

def main():

    """ 
    Coordinar el flujo completo: 
    scraping, parsing, objetos, bd, consultas y filtros
    """
    
    # Obtener el HTML
    html = ScraperEngine.fetch(URL)
    # Extraer datos
    countries_dict = CountryParser.parse_countries(html)

    countries = []

    for data in countries_dict:
        try:
            country = Country(**data)
            countries.append(country)
        except ValueError as e:
            print("Error de validación:", e)

    dao = CountryDAO("data/countries.db")

    dao.create_table()
    # Insertar todos los países
    dao.bulk_insert(countries)

    # Mostrar todos los países
    print("\n- - - - - TODOS - - - - -")
    print(dao.select_all()[:5])

    # Mostrar países con más de 100M de habitantes
    print("\n- - - - - MÁS DE 100M HAB - - - - -")
    print(dao.select_filtered(100_000_000))


if __name__ == "__main__":
    main()