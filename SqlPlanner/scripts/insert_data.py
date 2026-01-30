import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "sales.db"

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executescript("""
    INSERT INTO Brand VALUES
    (1, 'Dove', 'Personal Care'),
    (2, 'Surf Excel', 'Home Care'),
    (3, 'Lux', 'Personal Care'),
    (4, 'Rin', 'Home Care'),
    (5, 'Knorr', 'Food');

    INSERT INTO Product VALUES
    (1, 1, 'Dove Cream Beauty Bar 100g', 'DOV-CBB-100', 65.00),
    (2, 1, 'Dove Shampoo 180ml', 'DOV-SHP-180', 220.00),
    (3, 2, 'Surf Excel Easy Wash 1kg', 'SUR-EW-1KG', 145.00),
    (4, 2, 'Surf Excel Liquid 500ml', 'SUR-LIQ-500', 210.00),
    (5, 3, 'Lux Rose Soap 150g', 'LUX-RSE-150', 55.00),
    (6, 3, 'Lux Jasmine Soap 100g', 'LUX-JAS-100', 48.00),
    (7, 4, 'Rin Detergent Bar 250g', 'RIN-BAR-250', 30.00),
    (8, 4, 'Rin Powder 500g', 'RIN-PWD-500', 75.00),
    (9, 5, 'Knorr Tomato Soup 43g', 'KNR-TOM-043', 55.00),
    (10, 5, 'Knorr Veg Noodles 70g', 'KNR-NDL-070', 30.00);

    INSERT INTO Region VALUES
    (1, 'North India', 'India'),
    (2, 'South India', 'India'),
    (3, 'West India', 'India'),
    (4, 'East India', 'India'),
    (5, 'South East Asia', 'Multiple');

    INSERT INTO Customer VALUES
    (1, 'Reliance Retail Ltd', 'Retailer', 1),
    (2, 'DMart Stores', 'Retailer', 3),
    (3, 'Big Bazaar', 'Retailer', 1),
    (4, 'Metro Cash & Carry', 'Distributor', 2),
    (5, 'Flipkart Wholesale', 'E-commerce', 1),
    (6, 'Amazon India Seller Services', 'E-commerce', 1),
    (7, 'Spencer''s Retail', 'Retailer', 4),
    (8, 'More Supermarkets', 'Retailer', 2),
    (9, 'Future Consumer Distributors', 'Distributor', 3),
    (10, 'Udaan B2B Marketplace', 'E-commerce', 1),
    (11, 'Nilgiris Dairy Farm', 'Retailer', 2),
    (12, 'Vishal Mega Mart', 'Retailer', 4),
    (13, 'Adani Wilmar Trade Partners', 'Distributor', 3),
    (14, 'Tata Consumer Distribution', 'Distributor', 1),
    (15, 'Indomaret', 'Retailer', 5),
    (16, 'Alfamart', 'Retailer', 5),
    (17, 'Lotus’s Vietnam', 'Retailer', 5),
    (18, 'Saigon Co.op', 'Distributor', 5);

    INSERT INTO Sales VALUES
    (1, 1, 1, '2024-01-05', 500, 32500),
    (2, 2, 1, '2024-01-06', 200, 44000),
    (3, 3, 2, '2024-01-07', 800, 116000),
    (4, 4, 2, '2024-01-08', 300, 63000),
    (5, 5, 3, '2024-01-10', 600, 33000),
    (6, 6, 3, '2024-01-11', 700, 33600),
    (7, 7, 4, '2024-01-12', 1000, 30000),
    (8, 8, 4, '2024-01-13', 400, 30000),
    (9, 9, 5, '2024-01-14', 350, 19250),
    (10, 10, 5, '2024-01-15', 900, 27000),
    (11, 1, 6, '2024-01-16', 300, 19500),
    (12, 2, 6, '2024-01-17', 150, 33000),
    (13, 3, 8, '2024-01-18', 500, 72500),
    (14, 4, 8, '2024-01-19', 220, 46200),
    (15, 5, 7, '2024-01-20', 400, 22000),
    (16, 9, 10, '2024-01-21', 600, 33000),
    (17, 10, 10, '2024-01-22', 1200, 36000),
    (18, 1, 11, '2024-01-23', 250, 16250),
    (19, 3, 12, '2024-01-24', 450, 65250),
    (20, 5, 15, '2024-01-25', 700, 38500),
    (21, 6, 16, '2024-01-26', 900, 43200),
    (22, 9, 17, '2024-01-27', 500, 27500),
    (23, 10, 18, '2024-01-28', 1000, 30000),
    (24, 2, 14, '2024-01-29', 350, 77000),
    (25, 4, 13, '2024-01-30', 280, 58800);
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
