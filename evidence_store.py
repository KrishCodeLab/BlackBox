
import json
from pathlib import Path

DB_FILE = Path("blackbox_evidence.json")


def index_logs(log_entries):
    if DB_FILE.exists():
        logs = json.loads(DB_FILE.read_text(encoding="utf-8"))
    else:
        logs = []

    existing_ids = {log["id"] for log in logs}

    for log in log_entries:
        if log["id"] not in existing_ids:
            logs.append(log)
            existing_ids.add(log["id"])

    DB_FILE.write_text(
        json.dumps(logs, indent=2),
        encoding="utf-8",
    )


def retrieve_evidence(query, limit=5):
    if not DB_FILE.exists():
        return []

    logs = json.loads(DB_FILE.read_text(encoding="utf-8"))
    terms = query.lower().split()

    scored = []

    for log in logs:
        text = log["message"].lower()
        score = sum(term in text for term in terms)

        if score > 0:
            scored.append((score, log))

    scored.sort(key=lambda item: item[0], reverse=True)

    return [log for score, log in scored[:limit]]


if __name__ == "__main__":
    sample_logs = [
        {
            "id": "log1",
            "timestamp": "10:00:01",
            "level": "INFO",
            "service": "api",
            "message": "API server started",
        },
        {
            "id": "log2",
            "timestamp": "10:00:03",
            "level": "WARN",
            "service": "database",
            "message": "Database latency elevated",
        },
        {
            "id": "log3",
            "timestamp": "10:00:05",
            "level": "ERROR",
            "service": "database",
            "message": "Database connection timeout",
        },
        {
            "id": "log4",
            "timestamp": "10:00:06",
            "level": "ERROR",
            "service": "payments",
            "message": "Payment request failed",
        },
    ]

    index_logs(sample_logs)
    results = retrieve_evidence("database connection failure", limit=3)

    print("\nBLACKBOX - Retrieved Evidence\n")
    for item in results:
        print(item)
