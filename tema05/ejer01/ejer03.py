# EJERCICIO 3. ENCAPSULAMIENTO

# 1. clase 'Biblioteca'
class Biblioteca:
    # método constructor
    def __init__(self, num_libros):
        # 1. atributo 'num_libros' privado
        self.__num_libros = num_libros
    
    # 2. método que imprime el número de libros
    def ver_num_libros(self):
        print(f"El número total de libros es: {self.__num_libros}")
        
    # 2. método que añade una cantidad de libros
    def agregar_libros(self, cantidad):
        self.__num_libros += cantidad
        
# 3. objeto 'Biblioteca' con atributo 'num_libros' iniciado a 100
biblio1 = Biblioteca(100)

# 3. imprimir el número de libros
biblio1.ver_num_libros()

# 4. agregar 50 libros
biblio1.agregar_libros(50)

# 4. imprimir el número de libros
biblio1.ver_num_libros()