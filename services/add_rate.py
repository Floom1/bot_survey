import sqlite3
from services.generate_id import generate_unique_id


def add_rating(rate):
    if not (1 <= rate <= 10):
        raise ValueError("Rate must be between 1 and 10.")
    conn = sqlite3.connect("bot_ratings.db")
    cursor = conn.cursor()
    id_meeting = generate_unique_id()
    cursor.execute("INSERT INTO ratings (id_meeting, rate) VALUES (?, ?)", (id_meeting, rate))
    conn.commit()
    conn.close()
    return id_meeting
