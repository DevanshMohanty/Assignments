import json
from pathlib import Path


def load_json(path):
    path = Path(path)

    # If file does not exist → empty memory
    if not path.exists():
        return []

    # If file exists but is empty → empty memory
    if path.stat().st_size == 0:
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Invalid JSON → reset safely
        return []


def save_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
