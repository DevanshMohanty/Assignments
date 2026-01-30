# schema/grounding.py
from src.schema.schema import SCHEMA


def render_schema() -> str:
    lines = []

    for table, info in SCHEMA.items():
        lines.append(f"Table {table}")
        lines.append(f"  Columns: {', '.join(info['columns'])}")
        lines.append(f"  Primary key: {info['primary_key']}")

        fks = info.get("foreign_keys", {})
        for col, ref in fks.items():
            lines.append(f"  Foreign key: {table}.{col} -> {ref}")

        lines.append("")

    return "\n".join(lines)
