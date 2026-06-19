import sqlite3

DB_NAME = "battleship.db"


def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        games_played INTEGER DEFAULT 0,
        games_won INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def save_player(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO players(username) VALUES(?)",
        (username,)
    )

    conn.commit()
    conn.close()