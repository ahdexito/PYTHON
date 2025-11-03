# EJERCICIO 04

class GuiaTuristico:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print("Bienvenidos al tour.")
        
        
class GuiaMuseo(GuiaTuristico):  
    def __init__(self, nombre, idioma):
        super().__init__(nombre)
        self.idioma = idioma
    
    def hablar(self):
        print(f"Hola, soy {self.nombre}, y hablaré en {self.idioma}.")
        
    def presentar(self):
        self.hablar()
        super().hablar()
        

guia1 = GuiaMuseo("Eustaquio", "español")
guia1.presentar()