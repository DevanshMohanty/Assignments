import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "db" / "sales.db"


def extract_schema():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    schema = {}

    # Get all tables
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%';
    """)
    tables = [row["name"] for row in cursor.fetchall()]

    for table in tables:
        schema[table] = {
            "columns": {},
            "primary_key": [],
            "foreign_keys": []
        }

        # Columns + PK
        cursor.execute(f"PRAGMA table_info({table});")
        for col in cursor.fetchall():
            schema[table]["columns"][col["name"]] = col["type"]
            if col["pk"]:
                schema[table]["primary_key"].append(col["name"])

        # Foreign keys
        cursor.execute(f"PRAGMA foreign_key_list({table});")
        for fk in cursor.fetchall():
            schema[table]["foreign_keys"].append({
                "column": fk["from"],
                "ref_table": fk["table"],
                "ref_column": fk["to"]
            })

    conn.close()
    return schema


if __name__ == "__main__":
    from pprint import pprint
    pprint(extract_schema())
