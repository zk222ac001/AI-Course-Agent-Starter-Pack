"""Ordinary Python tools; no model required."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("lessons.json")

def get_lesson(week: int) -> str:
    """Look up the lesson for a course week.

    Args:
        week: Positive integer course week, such as 3.
    """
    if type(week) is not int or week < 1:
        return "Error: week must be a positive integer."
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return "Error: lesson data must be a JSON object."
        return json.dumps(data.get(str(week), {
            "status": "not_found", "message": "No lesson for this week."
        }), ensure_ascii=False)
    except (OSError, json.JSONDecodeError):
        return "Error: lessons.json is missing, unreadable, or invalid."

if __name__ == "__main__":
    print(get_lesson(3))

