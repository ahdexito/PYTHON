import sqlite3

class CountryDAO:
    
    def __init__(self, db_path: str):
        """ Inicializar conexión a SQLite """
        self.db_path = db_path
        
    def create_table(self):
        """ Crear la tabla si no existe """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS countries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        population INTEGER NOT NULL,
                        density INTEGER
                    );
                """)
            
        except sqlite3.Error as e:
            raise Exception(f"Error creando la tabla: {e}")


    def insert(self, country):
        """ Insertar un país """
        try:
            with sqlite3.connect(self.dp_path) as conn:
                # Borrar registros previos
                conn.execute("DELETE FROM countries;")
                # Reiniciar los IDs
                conn.execute("DELETE FROM sqlite_sequence WHERE name='countries';")
                # Insertar los nuevos
                conn.execute("""
                    INSERT INTO countries (name, population, density)
                    VALUES (?, ?, ?);
                """, (country.name, country.population, country.density))
                
        except sqlite3.Error as e:
            raise Exception(f"Error insertando país: {e}")
        
        
    def bulk_insert(self, countries):
        """ Insertar múltiples países """
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Borrar registros previos
                conn.execute("DELETE FROM countries;")
                # Reiniciar los IDs
                conn.execute("DELETE FROM sqlite_sequence WHERE name='countries';")
                # Insertar los nuevos
                conn.executemany("""
                    INSERT INTO countries (name, population, density)
                    VALUES (?, ?, ?);
                    """, [
                        (c.name, c.population, c.density)
                        for c in countries
                    ])
                
        except sqlite3.Error as e:
            raise Exception(f"Error en la inserción masiva: {e}")
        
        
    def select_all(self):
        """ Devolver todos los registros """
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                "SELECT * FROM countries;"
            ).fetchall()
            
            
    def select_filtered(self, min_population):
        """ Filtrar por población mínima """
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                "SELECT * FROM countries WHERE population > ?;",
                (min_population,)
            ).fetchall()