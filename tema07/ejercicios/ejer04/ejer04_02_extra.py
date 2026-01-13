import requests

def safe_get(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        return response.text
    
    except requests.exceptions.RequestException as e:
        return f"Error al acceder a la URL: {e}"