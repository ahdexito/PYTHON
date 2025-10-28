# EJERCICIO 01

class ReservaHotel:
    # atributo de clase
    agencia = "ViajesTorrevieja"
    
    # método de instancia
    def __init__(self, cliente, noches):
        # atributos de instancia
        self.cliente = cliente
        self.noches = noches
        
    # método de instancia
    def mostrar_reserva(self):
        print(f"Cliente: {self.cliente}; Noches: {self.noches}.")
    
    # método de clase
    def mostrar_agencia(cls):
        print(f"Nombre de la agencia: {cls.agencia}.")
      
    # método estático
    def mensaje_bienvenida():
        print("Bienvenido al sistema de reservas.")

# Prueba de métodos

# inicializar objetos
reserva1 = ReservaHotel("Diego", 3)
reserva2 = ReservaHotel("Estela", 5)

# métodos de instancia
reserva1.mostrar_reserva()
reserva2.mostrar_reserva()

# métodos de clase
reserva1.mostrar_agencia()
reserva2.mostrar_agencia()

# método estático
ReservaHotel.mensaje_bienvenida()