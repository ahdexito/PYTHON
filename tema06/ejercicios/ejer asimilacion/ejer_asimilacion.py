import json
import csv
import os

class Estudiante:
    def __init__(self, nombre, edad, nota, grupo):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        self.grupo = grupo
        
    # convertir objeto a diccionario
    def to_dict(self):
        return {"nombre":self.nombre,"edad":self.edad,"nota":self.nota,"grupo":self.grupo}
    
    # convertir objeto a string
    def __str__(self):
        return f"Nombre: {self.nombre}; Edad: {self.edad}; Nota: {self.nota}; Grupo: {self.grupo}"
    
    
# diccionario de estudiantes    
estudiantes = [
    Estudiante("Ricardo", 23, 8.4, "a"),
    Estudiante("Patricia", 26, 9.1, "b"),
    Estudiante("Enrique", 21, 7.3, "a")
]

# recoger datos si existen
if os.path.exists("estudiantes_extra.json"):
    with open("estudiantes_extra.json", "r", encoding="utf-8") as f:
        datos_extra = json.load(f)
        
    for e in datos_extra:
        estudiantes.append(
            Estudiante(
                e["nombre"],
                e["edad"],
                e["nota"],
                e["grupo"]
            )
        )

# agregar estudiantes nuevos y previos al json       
with open("datos_estudiantes.json", "w", encoding="utf-8") as f:
    json.dump([estudiante.to_dict() for estudiante in estudiantes], f, indent=4)
    
# cargar datos del json
with open("datos_estudiantes.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# reconstruir los datos
estudiantes_recuperados = [Estudiante(d["nombre"], d["edad"], d["nota"], d["grupo"]) for d in datos]

# imprimir estudiantes
print("\nLISTA COMPLETA DE ESTUDIANTES")
for estudiante in estudiantes_recuperados:
    print(estudiante)

# filtrar estudiantes
print("\nESTUDIANTES CON BUENAS NOTAS (>8)")
for estudiante in estudiantes_recuperados:
    if estudiante.nota >= 8:
        print(estudiante)

# calcular e imprimir media    
media = sum(e.nota for e in estudiantes_recuperados) / len(estudiantes_recuperados)
print("\nMEDIA GENERAL DE NOTAS")
print(round(media, 2))

# cargar datos a csv
with open("alumnos_completo.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Edad", "Nota", "Grupo"])
    for estudiante in estudiantes_recuperados:
        writer.writerow([estudiante.nombre, estudiante.edad, estudiante.nota, estudiante.grupo])