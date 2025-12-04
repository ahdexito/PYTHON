import requests

url = "https://www.httpbin.org/get"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Código de estado HTTP: {response.status_code}")
        
        print(f"Longitud del contenido HTML: {len(response.text)}")
        
        print(f"Contenido en formato JSON:")
        datos_json = response.json()
        print(datos_json)
        
        print(f"Dirección IP del cliente: {datos_json["origin"]}")
        
except requests.exceptions.RequestException as e:
    print("Error de conexión: {e}")