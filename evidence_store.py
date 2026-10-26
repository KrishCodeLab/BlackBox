
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
        log_id = str(log["id"])

        if log_id not in existing_ids:
            saved_log = {
                "id": log_id,
                "timestamp": log.get("timestamp", "Unknown"),
                "level": log.get("level", "UNKNOWN"),
                "service": log.get("service", "unknown"),
                "message": log.get("message", ""),
            }
            logs.append(saved_log)
            existing_ids.add(log_id)

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
        searchable_text = log["message"].lower()
        score = sum(term in searchable_text for term in terms)

        if score > 0:
            scored.append((score, log))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [log for score, log in scored[:limit]]


if __name__ == "__main__":
    from log_processor import parse_logs

    sample_text = Path("sample_logs.txt").read_text(encoding="utf-8")
    parsed_logs = parse_logs(sample_text)

    # Add the ID and service fields required by evidence storage.
    prepared_logs = []

    for i, log in enumerate(parsed_logs):
        prepared_logs.append({
            **log,
            "id": f"log{i + 1}",
            "service": "unknown",
        })

    index_logs(prepared_logs)

    print("\nBLACKBOX - Retrieved Evidence\n")
    for item in retrieve_evidence("database connection timeout", limit=3):
        print(item)
