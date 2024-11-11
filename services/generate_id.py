import random
import sqlite3


def generate_unique_id():
    conn = sqlite3.connect("bot_ratings.db")
    cursor = conn.cursor()
    while True:
        id_meeting = random.randint(0, 999999)
        cursor.execute("SELECT id_meeting FROM ratings WHERE id_meeting = ?", (id_meeting,))
        if not cursor.fetchone():
            conn.close()
            return id_meeting