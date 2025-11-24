import csv

# definición de la clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
        
    # método para convertir el objeto en diccionario
    def to_dict(self):
        return {"nombre":self.nombre,"edad":self.edad,"nota":self.nota}
    
    # representación legible
    def __str__(self):
        return f"{self.nombre}, {self.edad} años, nota: {self.nota}"
    
# crear una lista de objetos Estudiante
alumnos = [
    Estudiante("Ana", 20, 8.5),
    Estudiante("Luis", 19, 7.0),
    Estudiante("Carlos", 21, 9.2)
]

# guardar datos en CSV
with open("alumnos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Edad", "Nota"])
    for alumno in alumnos:
        writer.writerow([alumno.nombre, alumno.edad, alumno.nota])