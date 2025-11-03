# EJERCICIO 07

from abc import ABC, abstractmethod

class Excursion(ABC):
    @abstractmethod
    def duracion(self):
        pass
    
class ExcursionPlaya(Excursion):
    def duracion(self):
        print("La exurción a la playa dura 4 horas.")
        
class ExcursionMontanya(Excursion):
    def duracion(self):
        print("La excursión a la montaña dura 6 horas.")
        

playa = ExcursionPlaya()
montanya = ExcursionMontanya()

playa.duracion()
montanya.duracion()