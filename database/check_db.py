import sqlite3

DB_NAME = "database/users.db"

def show_users():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    if not users:
        print("No users found")

    else:
        print("Users:")
        for user in users:
            print(
                f"ID: {user[0]} | Default city: {user[1]}"
            )

    conn.close()


show_users()