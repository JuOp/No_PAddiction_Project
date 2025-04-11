
import sqlite3

class Database:
    @staticmethod
    def user_exists(user_id):
        with sqlite3.connect("bot.db") as conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, first_name TEXT)")
            c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return c.fetchone() is not None

    @staticmethod
    def register_user(user_id, username, first_name):
        try:
            with sqlite3.connect("bot.db") as conn:
                c = conn.cursor()
                c.execute("INSERT INTO users (id, username, first_name) VALUES (?, ?, ?)", (user_id, username, first_name))
                conn.commit()
                return True
        except Exception as e:
            print(e)
            return False
