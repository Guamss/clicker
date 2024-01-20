import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)

conn.execute("DROP TABLE IF EXISTS User")

conn.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE);""")