# AI Agents with Python — Classroom Starter Pack

For bachelor students taking their first elective in AI agents. All timetable data is fictional and editable.

## Start here

1. Install Python 3.11 or newer and [Ollama](https://ollama.com/download).
2. Extract this ZIP and open the extracted folder in VS Code.
3. Keep Ollama running. Open a terminal in the extracted folder.
4. On Windows, run:

~~~powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ollama pull llama3.2:3b
~~~

Activation is unnecessary with these commands. In VS Code select the .venv interpreter through **Python: Select Interpreter**.

## Run three stages

~~~powershell
.\.venv\Scripts\python.exe course_tools.py
.\.venv\Scripts\python.exe 01_chatbot.py
.\.venv\Scripts\python.exe 02_course_agent.py
~~~

On macOS/Linux create the environment with python3 and replace the Windows interpreter path with ./.venv/bin/python.

| File | Purpose |
|---|---|
| course_tools.py | Deterministic lookup without AI |
| 01_chatbot.py | Model without access to the timetable |
| 02_course_agent.py | Agent with visible tool requests and results |
| lessons.json | Editable course data |
| TEACHER_GUIDE.md | 90-minute lesson and demonstration script |
| STUDENT_ASSIGNMENT.md | Extension tasks and evaluation |
| TEACHER_SOLUTION.md | Example second tool |

## Try these questions

- What will we study in week 3?
- Compare weeks 2 and 3.
- What will we study in week 10?
- What will we study? (Expected: ask which week.)
- Explain a Python dictionary. (No course lookup needed.)

Edit lessons.json, save, and ask again. The tool rereads the file on every call; no retraining is required. JSON week keys are strings.

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

