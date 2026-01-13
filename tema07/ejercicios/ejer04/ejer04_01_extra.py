import requests

url = "https://httpbin.org/headers"

cabeceras = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)",
    "Accept-Language": "es-ES"
}

respuesta = requests.get(url, headers=cabeceras)

print(respuesta.json())