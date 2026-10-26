
import ollama

from log_processor import parse_logs

def investigate_incident(logs):
    print("BLACKBOX: Sending logs to Gemma...", flush=True)

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": f"""
Analyze these system logs.

1. Summarize the incident.
2. Identify the possible root cause.
3. Quote exact evidence from the logs.
4. Suggest three diagnostic steps.
5. Explain what is uncertain.

IMPORTANT RULES:
- Use only facts present in the logs.
- Never change timestamps or log messages.
- Never invent events or quotes.
- Separate confirmed facts from possible explanations.
- If evidence is missing, say so.

LOGS:
{logs}
"""
            }
        ]
    )

    print("BLACKBOX: Analysis received!", flush=True)

    return response["message"]["content"]




if __name__ == "__main__":
    with open("sample_logs.txt", "r") as file:
        raw_logs = file.read()

    parsed_logs = parse_logs(raw_logs)

    print("Logs processed successfully!")
    print(parsed_logs)

    result = investigate_incident(raw_logs)

    print("\n========== INVESTIGATION ==========\n")
    print(result)
