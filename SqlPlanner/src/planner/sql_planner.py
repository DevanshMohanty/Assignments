# planner/sql_planner.py
from llm import get_llm
from src.schema.grounding import render_schema


llm = get_llm()


PLANNER_PROMPT = """
You are a SQL query planner.

You are given a database schema.
You must ONLY use tables and columns from this schema.
Do NOT invent tables or columns.

Schema:
{schema}

User question:
{question}

Return a JSON plan with the following fields:
- tables: list of tables required
- joins: list of join conditions
- filters: list of WHERE conditions
- group_by: list of grouping columns
- metrics: list of aggregation expressions

Rules:
- Output ONLY valid JSON
- Use fully-qualified column names
- If no filter/group/metric is needed, return an empty list
"""


def generate_plan(question: str) -> dict:
    prompt = PLANNER_PROMPT.format(
        schema=render_schema(),
        question=question
    )

    response = llm.invoke(prompt)

    return response
    