"""Stage 1: a model without the course lookup tool."""
from ollama import Client

if __name__ == "__main__":
    client = Client(host="http://localhost:11434", timeout=120.0)
    question = input("You: ")
    response = client.chat(
        model="llama3.2:3b",
        messages=[
            {"role": "system", "content": "Be brief. Do not invent course details."},
            {"role": "user", "content": question},
        ],
        options={"temperature": 0},
    )
    print(response.message.content)

