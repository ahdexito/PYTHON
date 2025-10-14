# EJERCICIO 4. HERENCIA

# 1. clase 'Persona'
class Persona:
    # 1. atributo 'nombre'
    def __init__(self, nombre):
        self.nombre = nombre
    
    # 1. método 'presentarse', imprime el nombre
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
    
# 2. clase 'Profesor'
class Profesor(Persona):
    # 2. método 'enseñar'
    def ensenyar(self):
        print(f"Vamos a comenzar la clase.")
        
# 3. instancia de objeto 'Profesor'
profe1 = Profesor("Charles Xavier")

# 3. llamada a los métodos 'presentarse' y 'enseñar'
profe1.presentarse()

profe1.ensenyar()