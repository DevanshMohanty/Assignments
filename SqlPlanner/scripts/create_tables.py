import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "sales.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Brand (
        brand_id INTEGER PRIMARY KEY,
        brand_name TEXT,
        category TEXT
    );

    CREATE TABLE IF NOT EXISTS Product (
        product_id INTEGER PRIMARY KEY,
        brand_id INTEGER,
        product_name TEXT,
        sku TEXT,
        unit_price REAL,
        FOREIGN KEY (brand_id) REFERENCES Brand(brand_id)
    );

    CREATE TABLE IF NOT EXISTS Region (
        region_id INTEGER PRIMARY KEY,
        region_name TEXT,
        country TEXT
    );

    CREATE TABLE IF NOT EXISTS Customer (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        customer_type TEXT,
        region_id INTEGER,
        FOREIGN KEY (region_id) REFERENCES Region(region_id)
    );

    CREATE TABLE IF NOT EXISTS Sales (
        sales_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        customer_id INTEGER,
        sale_date DATE,
        quantity INTEGER,
        revenue REAL,
        FOREIGN KEY (product_id) REFERENCES Product(product_id),
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
