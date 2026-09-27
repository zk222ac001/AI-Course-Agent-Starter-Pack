"""Stage 1: a model without the course lookup tool."""
# Import the Ollama client class. The ollama Python package must be installed.
from ollama import Client

# Run this block only when this file is executed directly, not when imported.
if __name__ == "__main__":
    # Create a client for Ollama on this computer: localhost means this machine.
    # 11434 is the server port. The HTTP timeout setting is 120 seconds;
    # it is not an overall time budget for every operation in the program.
    client = Client(host="http://localhost:11434", timeout=120.0)
    # Display 'You: ', wait for Enter, and store what the user typed as a string.
    question = input("You: ")
    # Send a chat request and store the response. With default non-streaming,
    # the call waits for the response instead of printing generated pieces.
    response = client.chat(
        # Select the model installed in Ollama. This is its model name, not an API key.
        model="llama3.2:3b",
        # Start the list of messages sent to the model; each message is a dictionary.
        messages=[
            # The system message gives behavioral instructions. It does not supply timetable data.
            {"role": "system", "content": "Be brief. Do not invent course details."},
            # The user message contains the question entered at the keyboard.
            {"role": "user", "content": question},
        ],
        # Use low sampling randomness. This does not guarantee correct or identical answers.
        options={"temperature": 0},
    )
    # Extract the assistant message's text from the response object and display it.
    # This chatbot has no tools and does not read lessons.json.
    print(response.message.content)

