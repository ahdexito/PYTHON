import csv

with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "nota"])
    escritor.writerow(["Ana", 8.5])
    escritor.writerow(["Jorge", 6.0])
    escritor.writerow(["Marta", 9.2])