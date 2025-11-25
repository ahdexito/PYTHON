from abc import ABC, abstractmethod

# definir clase abstracta
class ServicioTuristico(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.__precio = precio
    
    # getter de precio    
    @property
    def precio(self):
        return self.__precio
    
    # setter de precio
    @precio.setter
    def precio(self, valor):
        # verificar que no sea negativo
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor
    
    # getter de nombre    
    @property
    def nombre(self):
        return self._nombre
    
    # definir método abstracto
    # las clase que hereden lo deberán implementar
    @abstractmethod
    def realizar_servicio(self):
        pass
    

# definir clase Excursion
# hereda de ServicioTurisico    
class Excursion(ServicioTuristico):
    def __init__(self, nombre, precio, destino, duracion_horas):
        # obtener los métodos y atributos de la superclase
        super().__init__(nombre, precio)
        # definir atributos propios
        self.destino = destino
        self.duracion_horas = duracion_horas
    
    # reescritura del método abstracto    
    def realizar_servicio(self):
        print(f"Realizando excursión a {self.destino} durante {self.duracion_horas} horas.")
    
    # convertir la información de la clase a String    
    def __str__(self):
        return f"Excursión({self._nombre}, precio: {self.precio}, destino: {self.destino}, duracion: {self.duracion_horas} h.)"
    __repr__ = __str__
    

# definir clase Alojamiento    
# hereda de ServicioTuristico
class Alojamiento(ServicioTuristico):
    def __init__(self, nombre, precio, nombre_hotel, estrellas):
        # obtener los métodos y atributos de la superclase
        super().__init__(nombre, precio)
        # definir atributos propios
        self.nombre_hotel = nombre_hotel
        self.estrellas = estrellas
        
    # reescritura del método abstracto
    def realizar_servicio(self):
        print(f"Reservando alojamiento {self.nombre_hotel} de {self.estrellas} estrellas.")
        
    # convertir la información de la clase a String
    def __str__(self):
        return f"Alojamiento({self.nombre}, precio: {self.precio}, hotel: {self.nombre_hotel}, estrellas: {self.estrellas})"
    __repr__ = __str__
    

# definir clase Transporte
# hereda de ServicioTuristico   
class Transporte(ServicioTuristico):
    def __init__(self, nombre, precio, tipo_transporte):
        # obtener los métodos y atributos de la superclase
        super().__init__(nombre, precio)
        # definir atributo propio
        self.tipo_transporte = tipo_transporte
    
    # reescritura del método abstracto    
    def realizar_servicio(self):
        print(f"Transportando a los clientes en {self.tipo_transporte}.")
    
    # convertir la información de la clase a String    
    def __str__(self):
        return f"Transporte({self._nombre}, precio: {self.precio}, tipo: {self.tipo_transporte})"
    __repr__ = __str__
    

# definir clase Agencia
# esta clase delega, contiene servicios pero no hereda  
class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios = []
    
    # añadir servicio a la lista de servicios    
    def agregar_servicio(self, servicio):
        # comprobar si el atributo recibido hereda de la clase ServicioTuristico
        if isinstance(servicio, ServicioTuristico):
            self.servicios.append(servicio)
    
    # imprimir cada servicio de la lista servicios        
    def mostrar_servicios(self):
        print(f"\nSERVICIOS DE LA AGENCIA {self.nombre}:")
        for s in self.servicios:
            print(s)
            
# método que ejecuta mostrar_servicios de cada subclase en la lista servicios            
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
print("\nEJECUCIÓN DE SERVICIOS:")
realizar_servicios(agencia)