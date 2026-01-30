import json
from src.schema.schema import SCHEMA


REQUIRED_KEYS = {"tables", "joins", "filters", "group_by", "metrics"}


class PlanValidationError(Exception):
    pass


def validate_plan(plan_text: str) -> dict:
    """
    Validates and returns a structured SQL plan.
    Raises PlanValidationError if invalid.
    """

    # Parse JSON
    try:
        plan = json.loads(plan_text)
    except json.JSONDecodeError as e:
        raise PlanValidationError(f"Invalid JSON: {e}")

    # Required keys
    missing = REQUIRED_KEYS - plan.keys()
    if missing:
        raise PlanValidationError(f"Missing keys: {missing}")

    # Validate tables
    for table in plan["tables"]:
        if table not in SCHEMA:
            raise PlanValidationError(f"Unknown table: {table}")

    # Validate columns helper
    def validate_column(col: str):
        if "." not in col:
            raise PlanValidationError(f"Unqualified column: {col}")

        table, column = col.split(".", 1)
        if table not in SCHEMA:
            raise PlanValidationError(f"Unknown table: {table}")

        if column not in SCHEMA[table]["columns"]:
            raise PlanValidationError(f"Unknown column: {col}")

    # Validate joins
    for join in plan["joins"]:
        if "=" not in join:
            raise PlanValidationError(f"Invalid join format: {join}")

        left, right = [x.strip() for x in join.split("=")]
        validate_column(left)
        validate_column(right)

    #  Validate filters
    for condition in plan["filters"]:
        column = condition.split()[0]
        validate_column(column)

    # Validate group by
    for col in plan["group_by"]:
        validate_column(col)

    # Validate metrics
    for metric in plan["metrics"]:
        if "(" not in metric or ")" not in metric:
            raise PlanValidationError(f"Invalid metric: {metric}")

        inner = metric[metric.find("(")+1:metric.find(")")]
        validate_column(inner)

    return plan
