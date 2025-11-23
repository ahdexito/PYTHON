import json
import csv

# leer json
with open("empleados.json", "r", encoding="utf-8") as f:
    empleados = json.load(f)
    
# crear archivo csv
with open("empleados.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    
    # cabecera
    escritor.writerow(["id", "nombre", "departamento", "salario"])
    
    # datos
    for e in empleados:
        escritor.writerow([
            e["id"],
            e["nombre"],
            e["departamento"],
            e["salario"]
        ])
        
# leer archivo csv
with open("empleados.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    next(lector)
    
    media = 0
    
    print("EMPLEADOS CON SALARIO MAYOR A 30000")
    for e_id, nombre, departamento, salario in lector:
        salario = float(salario)
        
        # sumar salario en cada iteración
        media += salario
        
        # imprimir si pasa el filtro
        if salario > 30000:
            print(f"Empleado/a: {nombre} | Salario: {salario:.2f}")
            
    # imprimir media     
    print("\nSALARIO MEDIO DE LOS EMPLEADOS")
    media /= 5
    print(f"Media: {media:.2f}")
    

with open("empleados_destacados.json", "w", encoding="utf-8") as f:
    