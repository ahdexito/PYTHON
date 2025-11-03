# EJERCICIO 06

class Transporte:
    def salir(self):
        print("El transporte está saliendo.")
        
class AutobusTuristico(Transporte):
    def salir(self):
        print("El autobús acaba de iniciar su ruta.")
        
class BarcoExcursion(Transporte):
    def salir(self):
        print("El barco ya ha zarpado.")
        
def iniciar_viaje(t):
    t.salir()
        

transporte = Transporte()
autobus = AutobusTuristico()
barco = BarcoExcursion()

iniciar_viaje(transporte)
iniciar_viaje(autobus)
iniciar_viaje(barco)