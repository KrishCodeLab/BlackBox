
import ollama

print("Connecting to Gemma...", flush=True)

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print("Gemma replied:", flush=True)
print(response["message"]["content"])
