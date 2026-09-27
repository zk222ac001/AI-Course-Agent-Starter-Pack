"""Ordinary Python tools; no model required."""
# Import Python's built-in JSON module: loads() reads JSON text; dumps() creates JSON text.
import json
# Import Path, a convenient way to build file paths and read files.
from pathlib import Path

# __file__ is this Python file's path. with_name() points to lessons.json beside it,
# so the lookup does not depend on the terminal's current folder.
DATA_FILE = Path(__file__).with_name("lessons.json")

# Define a reusable function. week is its input; : int and -> str are type hints.
# Type hints describe expected types but do not enforce them at runtime.
# The docstring below describes the tool; Ollama uses it when building its schema.
def get_lesson(week: int) -> str:
    """Look up the lesson for a course week.

    Args:
        week: Positive integer course week, such as 3.
    """
    # Reject an input unless it is an actual integer greater than zero.
    # 'or' short-circuits: Python checks week < 1 only if the type check passes.
    # The exact type check also rejects True and False, which Python otherwise treats as integers.
    if type(week) is not int or week < 1:
        # Stop this function immediately and return an explanatory error string.
        return "Error: week must be a positive integer."
    # Try the file-reading/parsing steps; matching failures go to the except block.
    try:
        # Read the file as UTF-8 text, then convert that JSON text into Python objects.
        # For this timetable, the outer JSON object should become a dictionary.
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        # Check the parsed structure: the timetable must be a dictionary, not a list or number.
        if not isinstance(data, dict):
            # Return an error before attempting a dictionary lookup on the wrong structure.
            return "Error: lesson data must be a JSON object."
        # Convert week to a string because JSON keys are strings: 3 becomes '3'.
        # data.get() returns the matching lesson, or the fallback dictionary below.
        # json.dumps() converts that result into a string to send back to the model.
        return json.dumps(data.get(str(week), {
            # These fallback fields explicitly report that the requested week is unavailable.
            "status": "not_found", "message": "No lesson for this week."
        # Finish the fallback and lookup. ensure_ascii=False preserves characters such as æ, ø, and å.
        }), ensure_ascii=False)
    # Catch file-access problems (OSError) and invalid JSON syntax (JSONDecodeError).
    except (OSError, json.JSONDecodeError):
        # Return a readable error so the caller can report the problem.
        return "Error: lessons.json is missing, unreadable, or invalid."

# Run the following demo only when this file is started directly.
# Importing get_lesson from another file will not run this demo.
if __name__ == "__main__":
    # Call the function for week 3, then print its returned string. No model is needed.
    print(get_lesson(3))

