
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
        level = parts[1]
        message = parts[2]

        logs.append({
            "timestamp": timestamp,
            "level": level,
            "message": message
        })

    return logs


if __name__ == "__main__":
    sample_logs = """
10:00:01 INFO API server started
10:00:03 WARN Database response time elevated
10:00:05 ERROR Database connection timeout
10:00:06 ERROR Payment request failed
10:00:08 ERROR Retry limit exceeded
"""

    result = parse_logs(sample_logs)

    for log in result:
        print(log)
