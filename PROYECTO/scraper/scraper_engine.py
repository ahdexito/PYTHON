import requests

class ScraperEngine:
    
    @staticmethod
    def fetch(url: str) -> str:
        """
        Descargar el contenido HTML de una URL.
        Lanza excepción si hay error HTTP o de red.
        """
        try:
            # Enviar la solicitud GET con cabeceras para simular navegador
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            response = requests.get(url, headers=headers)
            # Lanzar excepción si hay error HTTP
            response.raise_for_status()
            # Devolver HTML como string
            return response.text
        
        except requests.exceptions.RequestException as e:
            # Capturar cualquier fallo de red o respuesta HTTP inválida
            raise Exception(f"Error en la capa de scraping: {e}")