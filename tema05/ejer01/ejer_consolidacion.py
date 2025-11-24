class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__prestado = False
        
    def esta_prestado(self):
        return self.__prestado
        
    def prestar(self):
        self.__prestado = True
    
    def devolver(self):
        self.__prestado = False
    
        
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        
    def tomar_libro(self, libro):
        if not libro.esta_prestado():
            libro.prestar()
            self.libros.append(libro)
            return True
        return False
        
    def devolver_libro(self, libro):
        if libro in self.libros:
            libro.devolver()
            self.libros.remove(libro)
            return True
        return False

        
class Bibliotecario(Usuario):
    def agregar_libro(self, biblioteca, libro):
        biblioteca.append(libro)
        
        
class Invitado(Usuario):
    def tomar_libro(self, libro):
        if len(self.libros) == 0:
            return super().tomar_libro(libro)
        return False
            

biblioteca = []

libro1 = Libro("El Quijote", "Miguel de Cervantes")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez")

usuario1 = Usuario("Martín")
usuario2 = Usuario("Laura")
usuario3 = Invitado("Pedro")
usuario4 = Bibliotecario("Marta")


print("\nAGREGAR LIBROS A BIBLIOTECA")

usuario4.agregar_libro(biblioteca, libro1)
print("* Total de libros: ", len(biblioteca))

usuario4.agregar_libro(biblioteca, libro2)
print("* Total de libros: ", len(biblioteca))

usuario4.agregar_libro(biblioteca, libro3)
print("* Total de libros: ", len(biblioteca))


print("\nPRESTAR LIBROS A USUARIOS")

if usuario1.tomar_libro(libro1):
    print(f"* {usuario1.nombre} ha tomado el libro {libro1.titulo}")

if usuario2.tomar_libro(libro2):
    print(f"* {usuario2.nombre} ha tomado el libro {libro2.titulo}")

if usuario3.tomar_libro(libro3):
    print(f"* {usuario3.nombre} ha tomado el libro {libro3.titulo}")

if not usuario3.tomar_libro(libro2):
    print(f"* {usuario3.nombre} NO ha tomado el libro {libro2.titulo}")


print("\nRECIBIR PRESTACIONES DE LIBROS DE USUARIOS")

if usuario1.devolver_libro(libro1):
    print(f"* {usuario1.nombre} ha devuelto el libro {libro1.titulo}")

if usuario3.devolver_libro(libro3):
    print(f"* {usuario3.nombre} ha devuelto el libro {libro3.titulo}")