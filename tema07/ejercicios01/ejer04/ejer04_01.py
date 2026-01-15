import requests

url = "https://httpbin.org/headers"

cabeceras = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "es-ES"
}

respuesta = requests.get(url, headers=cabeceras)

print(respuesta.json())