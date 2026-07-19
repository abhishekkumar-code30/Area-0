import requests

OLLAMA_URL = "https://ollama.com/api"
API_KEY = "72e74515942743bdb5cb607204dee87d.2V6U6vAKNAk3liyxEuhpra_V"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

messages =[]

while True:
    user_input = input("\nYou: ")

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "gemma4:31b",
        "messages": messages,
        "stream": False
    }

    response = requests.post(f"{OLLAMA_URL}/chat", headers=headers, json=payload)
    result = response.json()

    assistant_message = result["message"]["content"]
    if user_input.lower() == "/exit":
        print("Goodbye!")
        break

    if not user_input:
        print("(empty input, try again)")
        continue
    messages.append({"role": "assistant", "content": assistant_message})

    print(f"\nMark 1: {assistant_message}")
