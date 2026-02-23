class Country:
    def __init__(self, name: str, population: int, density: int):
        """
        Modelo de dominio Country.
        Valida los datos antes de crear la instancia.
        """
        
        if not name or not name.strip():
            raise ValueError("El nombre del país no puede estar vacío")

        if not isinstance(population, int) or population <= 0:
            raise ValueError("La población debe ser un entero positivo")
        
        if density is not None and (not isinstance(density, int) or density < 0):
            raise ValueError("La densidad debe ser un entero >= 0")
        
        self.name = name.strip()
        self.population = population
        self.density = density
        
    # MÉTODOS DE DOMINIO
    
    def is_high_population(self, threshold=50_000_000) -> bool:
        """ Indica si el país supera un umbral de población """
        return self.population > threshold

    def is_dense(self, threshold=300) -> bool:
        """ Indica si el país tiene alta densidad """
        return self.density is not None and self.density > threshold

    # REPRESENTACIONES

    def __str__(self):
        return f"{self.name} - Población: {self.population:,}"
    
    def __repr__(self):
        return f"Country(name='{self.name}', population={self.population}, density={self.density})"
        