import sqlite3

class ProductDAO:
    def __init__(self, db_path="tienda.db"):
        self.db_path = db_path
        self.create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio TEXT NOT NULL,
                stock TEXT NOT NULL,
                url TEXT NOT NULL
            )
            """)
            conn.commit()

    def insert(self, product):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO products (nombre, precio, stock, url) VALUES (?, ?, ?, ?)",
                (product.nombre, product.precio, product.stock, product.url)
            )
            conn.commit()

    def bulk_insert(self, products):
        datos = [(p.nombre, p.precio, p.stock, p.url) for p in products]
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(
                "INSERT INTO products (nombre, precio, stock, url) VALUES (?, ?, ?, ?)",
                datos
            )
            conn.commit()

    def select_all(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, precio, stock, url FROM products")
            return cursor.fetchall()

    def select_in_stock(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, precio, stock, url FROM products WHERE stock = 'Sí'")
            return cursor.fetchall()
        
    def delete_all(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products")
            conn.commit()