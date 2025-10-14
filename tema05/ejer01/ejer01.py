class Libro:
    tipo = "literatura"
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    libro1 = Libro("El Quijote", "Miguel de Cervantes")
    
    print(f"Título: ", libro1.titulo)