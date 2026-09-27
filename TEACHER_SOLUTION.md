# Teacher Solution — Second Tool

Add to course_tools.py:

~~~python
def get_assignment(week: int) -> str:
    """Find the assignment for a course week.

    Args:
        week: Positive integer course week.
    """
    if type(week) is not int or week < 1:
        return "Error: week must be a positive integer."
    assignments = {
        3: "Build a course assistant and record five evaluation cases.",
        4: "Retrieve document passages and cite their sources.",
    }
    return assignments.get(week, "No assignment information for this week.")
~~~

Replace the import and dictionary in 02_course_agent.py:

~~~python
from course_tools import get_lesson, get_assignment

AVAILABLE_TOOLS = {
    "get_lesson": get_lesson,
    "get_assignment": get_assignment,
}
~~~

The tools list is already derived from AVAILABLE_TOOLS. Add to the system instruction:

> Use get_assignment for assignment questions. Use both tools when both lesson and assignment are requested.

Expected evidence: requests for the lesson and assignment for week 3, then a response supported by both. Order may vary. Record failures instead of hiding them.

Example new lessons to insert into the JSON object (add a comma after the preceding entry):

~~~json
"5": {"topic": "External APIs", "lab": "Call a read-only API"},
"6": {"topic": "Agent evaluation", "lab": "Compare traces with expected behavior"}
~~~

Teacher explanation: the model selects actions and arguments; Python enforces the allowlist, validates inputs, runs tools, and manages the loop. Editing JSON changes the lookup source, not model weights.

