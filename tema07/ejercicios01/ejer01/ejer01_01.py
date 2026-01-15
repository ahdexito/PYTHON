import requests

url = "https://www.httpbin.org/html"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Solicitud existosa. Contenido HTML:")
        print(response.text[:500])
    else:
        print(f"Error al obtener la página.Código de estado: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error de conexión: {e}")
    
texto = response.text

palabra = "Herman"
cantidad = texto.count(palabra)

print(f"La palabra {palabra} aparece {cantidad} vez/veces")