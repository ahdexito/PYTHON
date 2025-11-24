with open("datos.txt", "w") as f:
    f.write("Nombre: Ana\n")
    f.write("Edad: 22\n")
    f.write("Ciudad: Madrid")

with open("datos.txt", "r") as f:
    contenido = f.read()
    print(contenido)
