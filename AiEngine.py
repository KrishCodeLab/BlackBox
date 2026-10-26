
import ollama


def investigate_incident(logs):
    prompt = f"""
You are BLACKBOX, an AI incident investigation assistant.

Analyze the following system logs.

Your tasks:
1. Summarize what happened.
2. Identify the most likely root cause.
3. Quote the log entries that support your hypothesis.
4. Suggest three diagnostic steps.
5. State what cannot be determined from the available evidence.

Important rules:
- Do not invent log entries.
- Separate facts from hypotheses.
- If the evidence is insufficient, say so.
- Do not claim that a hypothesis is confirmed without sufficient evidence.

SYSTEM LOGS:
{logs}
"""

    try:
        response = ollama.chat(
            model="gemma3:1b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as error:
        return f"Investigation failed: {error}"


if __name__ == "__main__":
    sample_logs = """
    10:00:01 INFO API server started
    10:00:03 WARN Database response time elevated
    10:00:05 ERROR Database connection timeout
    10:00:06 ERROR Payment request failed
    10:00:08 ERROR Retry limit exceeded
    """

    print("\n========== BLACKBOX ==========\n")

    result = investigate_incident(sample_logs)

    print(result)
    
    print("\n==============================\n")
