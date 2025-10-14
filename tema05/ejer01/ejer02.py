# EJERCICIO 2. MÉTODOS Y SELF

# clase 'Libro'
class Libro:
    # variable de clase
    tipo = "literatura"
    
    # método constructor
    def __init__(self, titulo, autor):
        # atributos que recibe el método
        self.titulo = titulo
        self.autor = autor
        
    # 1. definir método 'presentar'
    def presentar(self):
        print(f"El libro '{self.titulo}' ha sido escrito por {self.autor}")

# creación de objeto 'libro'
libro1 = Libro("El Quijote", "Miguel de Cervantes")

# imprimir las variables del objeto
print(f"Título: {libro1.titulo}, Autor: {libro1.autor}")

# 2. creación de segundo objeto tipo 'Libro'
libro2 = Libro("El Resplandor", "Stephen King")

# 2. llamada al método 'presentar'
libro1.presentar()

libro2.presentar()