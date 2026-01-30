# main.py

from src.planner.sql_planner import generate_plan


def main():
    print("SQL Planner (Plan-only mode)")
    print("-" * 40)

    while True:
        question = input("\nAsk a question (or type 'exit'): ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Exiting...")
            break

        try:
            plan = generate_plan(question)
            print("\nGenerated Plan:")
            print(plan)

        except Exception as e:
            print("\nError generating plan:")
            print(str(e))


if __name__ == "__main__":
    main()
