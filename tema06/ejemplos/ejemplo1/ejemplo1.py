import json

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
    
# guardar la lista de objetos en un fichero JSON
with open("alumnos.json", "w") as f:
    json.dump([alumno.to_dict() for alumno in alumnos], f, indent=4)
    
# leer el fichero JSON y reconstruir los objetos
with open("alumnos.json", "r") as f:
    datos = json.load(f)
    
alumnos_recuperados = [Estudiante(d["nombre"], d["edad"], d["nota"]) for d in datos]

# mostrar los objetos reconstruidos
for alumno in alumnos_recuperados:
    print(alumno)