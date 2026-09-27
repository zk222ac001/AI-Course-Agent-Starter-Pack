# Teacher Guide — First AI Agent Lesson

![AI Agents with Python classroom learning path](assets/course-banner.svg)

**[← Project home](README.md) · [Full classroom walkthrough](CLASSROOM_WALKTHROUGH.md) · [Student assignment](STUDENT_ASSIGNMENT.md)**

> [!TIP]
> Project the [classroom walkthrough](CLASSROOM_WALKTHROUGH.md) during the lesson for colour-coded architecture, code explanations, and diagrams. Use this page as your teaching checklist.

**Duration:** 90 minutes  
**Prerequisites:** functions, dictionaries, loops, imports, basic exceptions  
**Outcome:** explain and modify a tool-using agent.

## Prepare before class

Install dependencies and download the model. Run all three stages and all five README prompts. If student computers are not ready, demonstrate centrally and let students work in pairs. Keep the solution until they have attempted the task.

## Explain the idea

“An agent uses a model to choose an available action. Our Python program checks the request, runs an allowed function, and returns its result. The model can answer or request another action.”

The model requests actions; Python executes them. Tool requests are structured data, not generated Python that we execute. The model chooses whether and which week to retrieve; the program constrains its choices.

| Minutes | Teacher activity | Student activity |
|---|---|---|
| 0–10 | Present the course lookup problem | Predict what information is needed |
| 10–20 | Run course_tools.py | Explain argument and result |
| 20–30 | Run 01_chatbot.py | Check whether the answer has course evidence |
| 30–45 | Run 02_course_agent.py | Identify request, execution, result, answer |
| 45–60 | Explain the loop | Explain each message role |
| 60–80 | Set the extension task | Add data and a second tool |
| 80–90 | Discuss traces and failures | Complete exit ticket |

## Live demo script

1. Run the direct lookup. Explain that this is ordinary Python.
2. Ask the chatbot about week 3. It may admit uncertainty or invent details. What evidence did it have?
3. Ask the agent the same question. Highlight the tool request and returned data.
4. Change week 3's lab in lessons.json, save, and ask again. No retraining happened.
5. Compare weeks 2 and 3. Observe whether both are retrieved in one or several model turns.
6. Ask about week 10. Check whether the final response respects the not-found result.
7. Ask “What will we study?” Look for clarification.

Illustrative trace, not a captured run:

~~~text
[Model turn 1]
[Tool requested] get_lesson: {'week': 3}
[Tool result] {"topic": "AI agents and Python tools", "lab": "Build a course assistant"}
[Model turn 2]
Assistant: In week 3 you study AI agents and Python tools...
~~~

## Walk through the code

1. get_lesson performs a deterministic lookup and validates the input.
2. AVAILABLE_TOOLS is an allowlist of executable functions.
3. messages holds system instructions, user input, assistant requests, and tool results.
4. client.chat sends context and tool descriptions to the model.
5. tool_calls contains requested actions.
6. **arguments unpacks named arguments into the selected function.
7. Appending the result lets the next model turn use it.
8. Stop conditions prevent an endless loop: final answer, five turns, or eight tool calls.

The SDK derives tool definitions from the function annotations and docstring. A schema helps the model form arguments; runtime validation is still needed. The trace shows observable actions, not hidden reasoning.

## Discussion

- Who selects the week? Who reads the file?
- Why is a fluent answer not evidence that a tool ran?
- What happens if we omit tool results from the history?
- Why validate arguments and limit turns?
- Can the final answer still misrepresent a correct tool result?
- Why does “What about next week?” fail to refer to a previous question here?

## Exit ticket

Explain the model's decision, Python's action, and one failure you tested.

## Next lessons

Progress to two tools, a read-only external API, document retrieval with citations, and conversation memory. Introduce frameworks after students understand this loop. Reading this small JSON object is not training or vector-based RAG.

