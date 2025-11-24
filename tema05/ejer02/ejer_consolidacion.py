from abc import ABC, abstractmethod

class ServicioTuristico(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.__precio = precio
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor
        
    @property
    def nombre(self):
        return self._nombre
    
    @abstractmethod
    def realizar_servicio(self):
        pass
    
    
class Excursion(ServicioTuristico):
    def __init__(self, nombre, precio, destino, duracion_horas):
        super().__init__(nombre, precio)
        self.destino = destino
        self.duracion_horas = duracion_horas
        
    def realizar_servicio(self):
        print(f"Realizando excursión a {self.destino} durante {self.duracion_horas} horas.")
        
    def __str__(self):
        return f"Excursión({self._nombre}, precio: {self.precio}, destino: {self.destino}, duracion: {self.duracion_horas} h.)"
    
    __repr__ = __str__
    
    
class Alojamiento(ServicioTuristico):
    def __init__(self, nombre, precio, nombre_hotel, estrellas):
        super().__init__(nombre, precio)
        self.nombre_hotel = nombre_hotel
        self.estrellas = estrellas
        
    def realizar_servicio(self):
        print(f"Reservando alojamiento {self.nombre_hotel} de {self.estrellas} estrellas.")
        
    def __str__(self):
        return f"Alojamiento({self.nombre}, precio: {self.precio}, hotel: {self.nombre_hotel}, estrellas: {self.estrellas})"
    
    __repr__ = __str__
    
    
class Transporte(ServicioTuristico):
    def __init__(self, nombre, precio, tipo_transporte):
        super().__init__(nombre, precio)
        self.tipo_transporte = tipo_transporte
        
    def realizar_servicio(self):
        print(f"Transportando a los clientes en {self.tipo_transporte}.")
        
    def __str__(self):
        return f"Transporte({self._nombre}, precio: {self.precio}, tipo: {self.tipo_transporte})"
    
    __repr__ = __str__
    
    
class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios = []
        
    def agregar_servicio(self, servicio):
        if isinstance(servicio, ServicioTuristico):
            self.servicios.append(servicio)
            
    def mostrar_servicios(self):
        print(f"Servicios de la agencia {self.nombre}:")
        for s in self.servicios:
            print(s)
            
            
def realizar_servicios(agencia):
    for s in agencia.servicios:
        s.realizar_servicio()
        
        
# crear servicios
excursion1 = Excursion("Tour Salinas", 50, "Salinas de Torrevieja", 3)
excursion2 = Excursion("Casco Histórico", 40, "Casco Histórico de Torrevieja", 2)
alojamiento1 = Alojamiento("Hotel Sol", 120, "Hotel Sol", 4)
transporte1 = Transporte("Traslado Puerto", 30, "autobús")
transporte2 = Transporte("Traslado Isla", 50, "barco")

# crear agencia
agencia = Agencia("ViajesTorrevieja")

# agregar servicios a la agencia
agencia.agregar_servicio(excursion1)
agencia.agregar_servicio(excursion2)
agencia.agregar_servicio(alojamiento1)
agencia.agregar_servicio(transporte1)
agencia.agregar_servicio(transporte2)

# mostrar todos los servicios
agencia.mostrar_servicios()

# ejecutar servicios polimórficamente
print("\nEjecutando servicios:")
realizar_servicios(agencia)