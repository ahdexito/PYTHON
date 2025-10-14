# EJERCICIO 1. CLASE SIMPLE Y ATRIBUTOS

# 1. clase Libro
class Libro:
    # 3. variable de clase
    tipo = "literatura"
    
    # 2. método constructor
    def __init__(self, titulo, autor):
        # 2. atributos que recibe el método
        self.titulo = titulo
        self.autor = autor

# 4. creación de objeto libro
libro1 = Libro("El Quijote", "Miguel de Cervantes")

# 5. imprimir las variables del objeto
print(f"Título: {libro1.titulo}, Autor: {libro1.autor}")