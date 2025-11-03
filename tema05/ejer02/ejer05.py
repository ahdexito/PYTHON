# EJERCICIO 05

class Online:
    def tipo(self):
        print("Visita online.")
        
class Presencial:
    def tipo(self):
        print("Visita presencial.")
        
class Ubicacion:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        
    def mostrar_coordenadas(self):
        print(f"Latitud: {self.latitud}, Longitud: {self.longitud}")
        
class VisitaMixta(Online, Presencial):
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.ubicacion = Ubicacion(latitud, longitud)
        
    def mostrar_info(self):
        print(f"Visita: {self.nombre}")
        
        print("Ubicación: ")
        self.ubicacion.mostrar_coordenadas()
        
        print("Tipo de visita:")
        self.tipo()
            
            
            
visita = VisitaMixta("Oceanografic", 39.4553, -0.3828)
visita.mostrar_info()

print("MRO:")
print(VisitaMixta.__mro__)