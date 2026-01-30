KEYWORD_TABLE_MAP = {
    "sales": ["Sales"],
    "revenue": ["Sales"],
    "quantity": ["Sales"],
    "product": ["Product"],
    "brand": ["Brand"],
    "category": ["Brand"],
    "customer": ["Customer"],
    "region": ["Region"],
    "country": ["Region"],
    "india": ["Region"],
}


def ground_schema(schema: dict, question: str) -> dict:
    question = question.lower()
    relevant_tables = set()

    for keyword, tables in KEYWORD_TABLE_MAP.items():
        if keyword in question:
            relevant_tables.update(tables)

    if any(word in question for word in ["total", "sum", "average", "revenue"]):
        relevant_tables.add("Sales")

    if not relevant_tables:
        return {
            "mode": "FULL_SCHEMA",
            "schema": schema
        }

    expanded = True
    while expanded:
        expanded = False
        for table in list(relevant_tables):
            for fk in schema[table]["foreign_keys"]:
                if fk["ref_table"] not in relevant_tables:
                    relevant_tables.add(fk["ref_table"])
                    expanded = True

    return {
        "mode": "PARTIAL_SCHEMA",
        "schema": {t: schema[t] for t in relevant_tables}
    }
