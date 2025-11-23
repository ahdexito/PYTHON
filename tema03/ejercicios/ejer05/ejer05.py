import json

with open("persona.json", "r") as f:
    persona = json.load(f)
    print(f"Nombre:", persona["nombre"], "-", "Edad:", persona["edad"])