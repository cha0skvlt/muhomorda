import sqlite3

def init_db():
    with sqlite3.connect("mukhomorda.db") as conn:
        with open("schema.sql", "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        print("[DB] Initialized.")

if __name__ == "__main__":
    init_db()
