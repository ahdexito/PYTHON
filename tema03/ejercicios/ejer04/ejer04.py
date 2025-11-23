import json

persona = {
    "nombre":"Lucía",
    "edad":30,
    "activo":True
}

with open("persona.json", "w") as f:
    json.dump(persona, f, indent=4)