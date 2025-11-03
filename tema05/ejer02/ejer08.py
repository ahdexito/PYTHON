# EJERCICIO 08

class PaqueteTuristico:
    def __init__(self, dias):
        self.dias = dias
        
    def __str__(self):
        print(f"Paquete turístico de {self.dias} días")
        
    def _repr__(self):
        print(f"PaqueteTuristico(dias={self.dias})")
        
    def __eq__(self, otro):
        if isinstance(otro, PaqueteTuristico):
            print(self.dias == otro.dias)
            return self.dias == otro.dias
        return False
    
    def __add__(self, otro):
        if isinstance(otro, PaqueteTuristico):
            nuevo = PaqueteTuristico(self.dias + otro.dias)
            print(f"Suma: {nuevo.dias} días")
            return nuevo
        return NotImplemented
    
    def __sub__(self, otro):
        if isinstance(otro, PaqueteTuristico):
            nuevo = PaqueteTuristico(self.dias - otro.dias)
            print(f"Resta: {nuevo.dias} días")
            return nuevo
        return NotImplemented
    
    def __lt__(self, otro):
        if isinstance(otro, PaqueteTuristico):
            print(self.dias < otro.dias)
            return self.dias < otro.dias
        return NotImplemented
    
    
p1 = PaqueteTuristico(5)
p2 = PaqueteTuristico(7)
p3 = PaqueteTuristico(5)

p1.__str__()
p2.__repr__()

p1.__eq__(p3)
p1.__eq__(p2)
p1.__lt__(p2)

p4 = p1 + p2
p5 = p2 - p1