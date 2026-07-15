import sqlite3


DB_NAME = "database/users.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        default_city TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_default_city(user_id, city):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (user_id, default_city)
    VALUES (?, ?)
    ON CONFLICT(user_id)
    DO UPDATE SET default_city=excluded.default_city
    """, (user_id, city))

    conn.commit()
    conn.close()


def get_default_city(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT default_city FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None