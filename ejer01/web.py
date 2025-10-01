import requests
url = "https://www.google.com"
response = requests.get(url)
print(f"La petición a {url} ha devuelto el código de estado: {response.status_code}")