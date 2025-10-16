# EJERCICIO 5. POLIMORFISMO

# clase 'Persona'
class Persona:
    # atributo 'nombre'
    def __init__(self, nombre):
        self.nombre = nombre
    
    # método 'presentarse', imprime el nombre
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
    
    
# 1. clase 'Profesor'
class Profesor(Persona):
    # método 'enseñar'
    def ensenyar(self):
        print("Vamos a comenzar la clase.")
    # 3. método 'hablar' que explica el tema
    def hablar(self):
        print("Voy a explicar el tema.")
       
       
# 1. clase 'Alumno'
class Alumno(Persona):
    # 2. método 'hablar' que pregunta una duda
    def hablar(self):
        print("Tengo una duda.")
 
 
# 4. función que llama al método 'hablar'       
def hacer_hablar(Persona):
    Persona.hablar()
    
# instancia de objeto 'Profesor'
profe1 = Profesor("Charles Xavier")

# instancia de objeto 'Alumno'
alumno1 = Alumno("Jaimito")

# 5. llamadas de la función 'hacer hablar'
alumno1.presentarse()
hacer_hablar(alumno1)

profe1.presentarse()
hacer_hablar(profe1)