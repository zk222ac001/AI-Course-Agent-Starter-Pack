# Assignment — Extend the Course Assistant

**[← Project home](README.md) · [Architecture and explanations](CLASSROOM_WALKTHROUGH.md)**

> [!IMPORTANT]
> **Your challenge:** extend the course assistant and show evidence of how it uses tools. Explain the model’s request, Python’s action, and the result.

**Time:** 30–45 minutes in pairs  
**Goal:** modify tools and explain evidence from an agent run.

## 🔵 A. Understand the baseline

Run the direct lookup and agent. Ask about week 3. Identify user input, tool name, arguments, result, and final answer.

## 🟣 B. Extend the data

Add weeks 5 and 6 to lessons.json, each with a topic and lab. Save and ask about both. Explain why retraining is unnecessary.

## 🟢 C. Add a tool

Create get_assignment(week: int) -> str with fictional assignments for weeks 3 and 4. Include a docstring, validate the week, and return an explicit message for unavailable data.

Import and register the function in AVAILABLE_TOOLS. The agent derives its tools list from this dictionary. Update the system instruction to use the assignment tool for assignment questions.

Ask: “What is the lesson and assignment for week 3?”

## 🟠 D. Evaluate actual behavior

| Input | Expected behavior | Actual tool calls | Pass/fail |
|---|---|---|---|
| Lesson for week 3? | Retrieve week 3 | | |
| Compare weeks 2 and 3 | Retrieve both | | |
| Lesson for week 10? | Report missing information | | |
| What will we study? | Ask which week | | |
| Lesson and assignment for week 3? | Use both relevant tools | | |

Also call get_lesson(-1) directly. Explain the result. Record failures honestly; do not assume the model behaves as intended.

## Submit

Submit your Python/JSON files, completed results table, and 150–250 words explaining the loop and one observed limitation.

| Criterion | Points |
|---|---:|
| Correct data extension | 2 |
| Working second tool and registration | 3 |
| Evidence from all five prompts | 3 |
| Clear model-versus-Python explanation | 2 |

**Extension:** preserve history across questions. Test “What about the next week?” and explain how memory changes behavior.

