
from log_processor import parse_logs, summarize_logs
from evidence_store import index_logs, retrieve_evidence
import ollama



def investigate_incident(logs):
    parsed_logs = parse_logs(logs)

    # Give every log a unique ID
    for i, log in enumerate(parsed_logs):
        log["id"] = f"log{i + 1}"

    # Store the logs
    index_logs(parsed_logs)

    # Search for relevant evidence
    evidence = retrieve_evidence("database connection payment error", limit=5)

    print("\nBLACKBOX: Retrieved evidence:")
    for item in evidence:
        print(item)

    print("\nBLACKBOX: Sending logs and evidence to Gemma...", flush=True)

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": f"""
Investigate this incident using the logs and retrieved evidence.

1. Summarize the incident.
2. Suggest a possible root cause.
3. Explain the evidence.
4. Suggest three diagnostic steps.
5. State what is uncertain.

Rules:
- Do not invent log entries or timestamps.
- Separate facts from possible explanations.
- Do not claim an event happened multiple times unless the logs prove it.
- If evidence is insufficient, say so.

ALL LOGS:
{logs}

RETRIEVED EVIDENCE:
{evidence}
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
