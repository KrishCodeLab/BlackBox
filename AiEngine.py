
from log_processor import parse_logs, summarize_logs
import ollama


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
3. Quote the evidence.
4. Suggest three diagnostic steps.
5. Mention what is uncertain.

Do not invent evidence.

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
    summary = summarize_logs(parsed_logs)

    print("\n========== LOG SUMMARY ==========")
    print(summary)

    print("\n========== BLACKBOX INVESTIGATION ==========")
    result = investigate_incident(raw_logs)
    print(result)
