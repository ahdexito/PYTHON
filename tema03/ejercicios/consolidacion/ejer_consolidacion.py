import json
import csv

class Empleado:
    def __init__(self, id, nombre, departamento, salario):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento
        self.salario = float(salario)
        
    def to_dict(self):
        return {"id":self.id,"nombre":self.nombre,"departamento":self.departamento,"salario":self.salario}

    def __str__(self):
        return f"* Id: {self.id}; Nombre: {self.nombre}; Departamento: {self.departamento}; Salario: {self.salario}"

# leer y descargar json
with open("empleados.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# reconstruir empleados a objetos en una lista
empleados = [
    Empleado(d["id"], d["nombre"], d["departamento"], d["salario"])
    for d in datos
]
    
# crear archivo csv y exportar datos
with open("empleados.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f) 
    # cabecera
    writer.writerow(["id", "nombre", "departamento", "salario"])
    # datos
    for e in empleados:
        writer.writerow([
            e.id,
            e.nombre,
            e.departamento,
            e.salario
        ])

# lista para almacenar empleados filtrados
empleados_filtrados = []
        
# leer archivo csv
with open("empleados.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    
    # filtrar y guardar empleados por filtro
    for e_id, nombre, departamento, salario in reader:
        salario = float(salario)
        # guardar si pasa el filtro
        if salario > 30000:
            empleados_filtrados.append(Empleado(e_id, nombre, departamento, salario))
            
    # imprimir empleados filtrados
    print("EMPLEADOS CON SALARIO MAYOR A 30000")
    for e in empleados_filtrados:
        print(e)
            
    # calcular e imprimir media     
    print("\nSALARIO MEDIO DE LOS EMPLEADOS")
    media = sum(e.salario for e in empleados) / len(empleados)
    print(f"Media: {media:.2f}")
    
# crear archivo json y cargar con empleados filtrados
with open("empleados_destacados.json", "w", encoding="utf-8") as f:
    json.dump([e.to_dict() for e in empleados_filtrados], f, indent=4)
