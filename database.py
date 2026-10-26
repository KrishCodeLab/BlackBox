
import sqlite3
import json

DB_NAME = "blackbox.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS investigations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            logs TEXT,
            summary TEXT,
            report TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_investigation(username, logs, summary, report):
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        INSERT INTO investigations
        (username, logs, summary, report)
        VALUES (?, ?, ?, ?)
    """, (
        username,
        logs,
        json.dumps(summary),
        report
    ))

    conn.commit()
    conn.close()


def get_investigations(username):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT *
        FROM investigations
        WHERE username = ?
        ORDER BY id DESC
    """, (username,)).fetchall()

    results = [dict(row) for row in rows]

    conn.close()
    return results
