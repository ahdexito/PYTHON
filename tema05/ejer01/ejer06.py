# EJERCICIO 6. ABSTRACCIÓN

# definir clase 'AulaVirtual'
class AulaVirtual:
    # atributo privado y oculto
    def __init__(self):
        self.__alumnos = 0
        
    # método que inicia la clase
    def iniciar_clase(self):
        print(f"La clase ha comenzado. Hay un total de {self.__alumnos} alumnos.")
        
    # método que añade nuevos alumnos
    def inscribir_alumnos(self, nuevos):
        self.__alumnos += nuevos
        
    # método que muestra el total de alumnos
    def numero_alumnos(self):
        print(f"El número total de alumnos inscritos es de {self.__alumnos}.")

# instancia de objeto
aula = AulaVirtual()

# llamada a cada método de su clase
aula.iniciar_clase()

aula.inscribir_alumnos(50)

aula.numero_alumnos()