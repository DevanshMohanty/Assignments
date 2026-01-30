from create_tables import create_tables
from insert_data import insert_data

def setup_database():
    create_tables()
    insert_data()
    print("Database setup completed successfully.")

if __name__ == "__main__":
    setup_database()
