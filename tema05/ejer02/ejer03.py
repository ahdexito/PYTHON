# EJERCICIO 03

class Habitacion:
    _precio_noche = 0
    
    def __init__(self, precio):
        self._precio_noche = precio
    
    @property
    def precio(self):
        return self._precio_noche
    
    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self._precio_noche = valor
            
    @precio.deleter
    def precio(self):
        del self._precio_noche
        
# inicializar objeto con valor determinado
habitacion = Habitacion(55)

# imprimir el valor de la variable
print("# Valor inicial:", habitacion.precio)

# asignar valor válido
habitacion.precio = 35

# imprimir el valor de la variable
print("# Nuevo valor válido:", habitacion.precio)

# asignar valor no válido
habitacion.precio = -23

# imprimir el valor de la variable
print("# Nuevo valor no válido", habitacion.precio)

# borrar atributo
del habitacion.precio

# imprimir el valor de la variable
print("# Valor eliminado", habitacion.precio)