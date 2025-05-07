#!/usr/bin/env python3

import sqlite3
import datetime

DB_PATH = "mukhomorda.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        with open("schema.sql", "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        print("[DB] Initialized.")

def is_duplicate_post(content: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT 1 FROM posts WHERE content = ? LIMIT 1", (content,))
    result = c.fetchone()
    conn.close()
    return result is not None

if __name__ == "__main__":
    init_db()
