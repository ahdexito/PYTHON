archivo = "log.txt"

with open(archivo, "w") as f:
    f.write("Inicio del registro\n")
    
with open(archivo, "a") as f:
    f.write("Segunda línea del registro")
    
with open(archivo, "r") as f:
    for linea in f:
        print(linea.strip())