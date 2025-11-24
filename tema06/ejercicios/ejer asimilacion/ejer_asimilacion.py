import json

class Estudiante:
    def __init__(self, nombre, edad, nota, grupo):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        self.grupo = grupo
        
estudiantes = [
    Estudiante("Ricardo", 23, 8.4, "a"),
    Estudiante("Patricia", 26, 9.1, "b"),
    Estudiante("Enrique", 21, 7.3, "a")
]

with open("alumnos_extra.json", "a") as f:
    