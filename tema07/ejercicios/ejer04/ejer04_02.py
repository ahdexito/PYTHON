import requests

url = "https://httpbin.org/status/404"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    print("Petición correcta")
    
except requests.exceptions.HTTPError as e:
    print("Error HTTP:", e)