
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
    sample_logs = """
    10:00:01 INFO API server started
    10:00:03 WARN Database response time elevated
    10:00:05 ERROR Database connection timeout
    10:00:06 ERROR Payment request failed
    10:00:08 ERROR Retry limit exceeded
    """
    result = investigate_incident(sample_logs)
    print(result)