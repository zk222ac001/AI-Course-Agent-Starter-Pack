![AI Agents with Python — learn the loop, build the tools, explain the decisions](assets/course-banner.svg)

# AI Agents with Python
### A classroom starter pack for your first tool-using agent

Build a course assistant that looks up lesson information, shows its tool calls, and explains the result. Designed for bachelor students learning Python and AI agents.

**[🧠 Start with theory](AI_AGENT_THEORY.md) · [📖 Classroom walkthrough](CLASSROOM_WALKTHROUGH.md) · [🎓 Teacher guide](TEACHER_GUIDE.md) · [🧪 Student assignment](STUDENT_ASSIGNMENT.md) · [🚀 Quick start](#-quick-start)**

> [!TIP]
> **Start with one question:** “What will we study in week 3?”  
> Run the same question through a Python lookup, a chatbot, and a tool-using agent. Watch what changes.

---

## 🧭 Your learning path

> [!IMPORTANT]
> **Start with the concepts:** [AI Agent Foundations — From Theory to Our Course Assistant](AI_AGENT_THEORY.md). Explain goals, environments, observations, actions, feedback, and autonomy before opening the Python code.
>
> **Suggested order:** 30-minute theory introduction → 90-minute practical walkthrough → student extension task.

The three practical stages follow the theory lesson:

| 🔵 01 · Python tool | 🟣 02 · Chatbot | 🟢 03 · AI agent |
|---|---|---|
| Retrieve a lesson with a function. | Ask a model without course data. | Let the model request the lookup. |
| **Learn:** arguments, dictionaries, results | **Learn:** prompts, messages, missing context | **Learn:** tool requests, execution, feedback |
| [Open course_tools.py](course_tools.py) | [Open 01_chatbot.py](01_chatbot.py) | [Open 02_course_agent.py](02_course_agent.py) |

> [!IMPORTANT]
> **The model requests the action. Python performs the action.**  
> The model selects an available tool and its arguments. The controller checks the request, runs the function, and returns its result.

## 🧠 See the architecture

![Course agent architecture: messages go to the model, Python executes requested tools, and results return to the conversation](assets/agent-architecture.svg)

**Read the diagram:** blue represents Python orchestration, violet represents the model, teal represents tool execution, and green represents the displayed response. Follow the return arrow to see the next model turn.

The full [classroom walkthrough](CLASSROOM_WALKTHROUGH.md#3-complete-project-architecture) includes an editable Mermaid flowchart, a sequence diagram, and explanations of every component.

## 🚀 Quick start

1. Install **Python 3.11 or newer** and [Ollama](https://ollama.com/download).
2. Clone this repository, or use **Code → Download ZIP** and extract it.
3. Open the project folder in VS Code and keep Ollama running.
4. Open a terminal in the project folder and run:

~~~powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ollama pull llama3.2:3b
~~~

In VS Code, use **Python: Select Interpreter** to select `.venv\Scripts\python.exe`. Activation is unnecessary when using the explicit interpreter paths above. If `.venv` already exists, skip the first command.

### Run one stage at a time

**01 — Ordinary Python**

~~~powershell
.\.venv\Scripts\python.exe course_tools.py
~~~

**02 — A model without the course lookup**

~~~powershell
.\.venv\Scripts\python.exe 01_chatbot.py
~~~

**03 — The agent with visible tool calls**

~~~powershell
.\.venv\Scripts\python.exe 02_course_agent.py
~~~

On macOS/Linux, create the environment with `python3 -m venv .venv` and replace the Windows interpreter path with `./.venv/bin/python`.

> [!NOTE]
> Local inference uses no paid API credits. Initial downloads require internet access, and speed depends on your computer. Download the model and rehearse before class. All timetable data is fictional and editable.

## 🔎 What a tool call looks like

Illustrative trace, not a captured live run:

~~~text
You: What will we study in week 3?

[Model turn 1]
[Tool requested] get_lesson: {'week': 3}
[Tool result] {"topic": "AI agents and Python tools",
               "lab": "Build a course assistant"}

[Model turn 2]
Assistant: In week 3, you study AI agents and Python tools.
The lab is to build a course assistant.
~~~

| Look for | What it demonstrates |
|---|---|
| 🟣 Tool requested | The model selected a function and arguments |
| 🟢 Tool result | Python executed the function and returned data |
| 🔵 Next model turn | The result was added to the conversation |
| ✅ Final response | The model used the information to answer |

## 🎓 Choose your classroom resource

| Resource | Use it for |
|---|---|
| [🧠 AI agent foundations](AI_AGENT_THEORY.md) | Start with general theory, then map each concept to our course assistant |
| [📖 Classroom walkthrough](CLASSROOM_WALKTHROUGH.md) | Projecting the full explanation, diagrams, and Python examples |
| [🧑‍🏫 Teacher guide](TEACHER_GUIDE.md) | Preparing a 90-minute lesson and live demonstrations |
| [🧪 Student assignment](STUDENT_ASSIGNMENT.md) | Extending the data, adding a second tool, and recording evaluations |
| [🔑 Teacher solution](TEACHER_SOLUTION.md) | Reviewing an example second tool after students attempt the task |

### Project map

| File | Responsibility |
|---|---|
| [course_tools.py](course_tools.py) | Validate input and retrieve course data |
| [01_chatbot.py](01_chatbot.py) | Demonstrate a model without the timetable |
| [02_course_agent.py](02_course_agent.py) | Manage tool requests, history, execution, and limits |
| [lessons.json](lessons.json) | Store the editable fictional timetable |
| [requirements.txt](requirements.txt) | Declare Python dependencies |
| [assets/](assets/) | Store the course banner and architecture illustration |

## 🧪 Try these questions

| Prompt | Watch for |
|---|---|
| What will we study in week 3? | A lookup for week 3 |
| Compare weeks 2 and 3. | Both weeks retrieved |
| What will we study in week 10? | An honest missing-information response |
| What will we study? | A clarification question |
| Explain a Python dictionary. | No course lookup needed |

> [!TIP]
> **A simple live experiment:** edit week 3 in `lessons.json`, save, and ask again. The tool rereads the file on every call. No model retraining is involved. JSON week keys are strings.

---

## Troubleshooting

| Symptom | Action |
|---|---|
| Python not found | Install Python and reopen terminal; try the Windows py launcher |
| Ollama command not found | Finish installation and reopen terminal |
| Connection refused | Start the Ollama app; CLI users can run ollama serve |
| Model not found | Run ollama pull llama3.2:3b |
| Missing module | Install requirements using the same .venv interpreter |
| Slow response or timeout | Close memory-heavy apps; rehearse on the teaching computer |
| Missing tool call or invented answer | Inspect the trace; test an explicit week question and discuss the failure |
| JSON error | Check double quotes and commas in lessons.json |

The local model requires no paid API credits. Initial downloads require internet access. Performance depends on the computer. Download and rehearse before class.

## Verification and limits

Python syntax and deterministic lookup/error cases were checked during preparation. Full Ollama/model interaction was not executed here. Run every prompt on your teaching computer before class. Tool selection and wording can vary; low temperature does not guarantee correctness.

The package does not include model weights or an installed environment. History resets for each question. This is a small tool-using agent with bounded autonomy.

## Official references

- [Tool calling](https://docs.ollama.com/capabilities/tool-calling)
- [Python SDK](https://github.com/ollama/ollama-python)
- [Llama 3.2](https://ollama.com/library/llama3.2)

