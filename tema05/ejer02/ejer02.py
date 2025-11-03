# EJERCICIO 02

class ReservaHotel:
    # atributo de clase
    agencia = "ViajesTorrevieja"
    
    # método de instancia
    def __init__(self, cliente, noches, precio_total):
        # atributos de instancia
        self.cliente = cliente
        self.noches = noches
        
        # atributo protegido
        self._precio_total = precio_total
        
        # atributo privado
        self.__codigo_confirmacion = 50
        
    # método getter
    def get_precio(self):
        return self._precio_total
    
    # método setter
    def set_precio(self, nuevo_precio):
        if nuevo_precio > self._precio_total:
            self._precio_total = nuevo_precio
        
    # método de instancia
    def mostrar_reserva(self):
        print(f"Cliente: {self.cliente}; Noches: {self.noches}.")
    
    # método de clase
    @classmethod
    def mostrar_agencia(cls):
        print(f"Nombre de la agencia: {cls.agencia}.")
      
    # método estático
    @staticmethod
    def mensaje_bienvenida():
        print("Bienvenido al sistema de reservas.")
        
    # método que reduce el precio si coincide el código
    def aplicar_descuento(self, porcentaje, codigo):
        if codigo == self.__codigo_confirmacion:
            self._precio_total -= self._precio_total * (porcentaje / 100)
    

# Prueba de métodos

# inicializar objetos
reserva1 = ReservaHotel("Diego", 3, 300)
reserva2 = ReservaHotel("Estela", 5, 250)


# probar método getter
print("# PROBAR MÉTODO GETTER")

print(f"  - Precio de reserva 1: {reserva1.get_precio()}")
print(f"  - Precio de reserva 2: {reserva2.get_precio()}")


# probar método setter
print("\n# PROBAR MÉTODO SETTER")

# precio inferior, no actualiza
reserva1.set_precio(100)
print(f"  - Precio de reserva 1: {reserva1.get_precio()}")

# precio superior, sí actualiza
reserva1.set_precio(400)
print(f"  - Precio de reserva 1: {reserva1.get_precio()}")


# probar método descuento
print("\n# PROBAR MÉTODO DESCUENTO")

# clave 5. no coincide, no aplica
reserva1.aplicar_descuento(30, 5)
print(f"  - Precio de reserva 1: {reserva1.get_precio()}")

# clave 50. coincide, aplica
reserva1.aplicar_descuento(30, 50)
print(f"  - Precio de reserva 1: {reserva1.get_precio()}")
