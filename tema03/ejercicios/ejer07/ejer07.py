import csv

with open("alumnos.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    next(lector)
    for nombre, nota in lector:
        nota = float(nota)
        
        if nota > 8.0:
            print(f"Alumno con buena nota: {nombre} ({nota})")