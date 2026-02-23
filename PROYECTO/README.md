-- URL UTILIZADA --

La fuente de datos es: https://www.worldometers.info/world-population/population-by-country/


-- DESCRIPCIÓN --

Este proyecto extrae información sobre la población de diferentes países del mundo y la guarda en una base de datos SQLite. Se sigue una arquitectura por capas para separar responsabilidades.

-Scraper: descarga el contenido HTML de la página.

-Parser: interpreta el HTML y extrae los datos relevantes.

-Modelos de dominio: representa a cada país como un objeto.

-DAO: gestiona la base de datos SQLite

-Programa principal: coordina el flujo, mostrando todos los países y filtrando según criterios.


-- ENTIDADES --

-Country:  representa un país con su población y densidad.

-CountryDAO: gestiona la persistencia de los objetos Country en la base de datos.