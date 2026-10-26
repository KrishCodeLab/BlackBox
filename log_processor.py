

def parse_logs(log_text):
    logs = []

    for line in log_text.splitlines():
        line = line.strip()

        if line == "":
            continue

        parts = line.split(" ", 2)

        if len(parts) < 3:
            logs.append({
                "timestamp": "Unknown",
                "level": "UNKNOWN",
                "message": line
            })
            continue

        timestamp = parts[0]
        level = parts[1].upper()
        message = parts[2]

        logs.append({
            "timestamp": timestamp,
            "level": level,
            "message": message
        })

    return logs


def summarize_logs(logs):
    summary = {
        "total": len(logs),
        "errors": 0,
        "warnings": 0,
        "info": 0,
        "unknown": 0
    }

    for log in logs:
        level = log["level"]

        if level == "ERROR":
            summary["errors"] += 1
        elif level in ["WARN", "WARNING"]:
            summary["warnings"] += 1
        elif level == "INFO":
            summary["info"] += 1
        else:
            summary["unknown"] += 1

    return summary


if __name__ == "__main__":
    sample_logs = """
10:00:01 INFO API server started
10:00:03 WARN Database response time elevated
10:00:05 ERROR Database connection timeout
10:00:06 ERROR Payment request failed
10:00:08 ERROR Retry limit exceeded
This is a malformed line

"""

    parsed_logs = parse_logs(sample_logs)
    summary = summarize_logs(parsed_logs)

    print("PROCESSED LOGS:")
    for log in parsed_logs:
        print(log)

    print("\nLOG SUMMARY:")
    print(summary)
