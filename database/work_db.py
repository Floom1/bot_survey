import sqlite3

def add_rating(id_meeting, rate):
    conn = sqlite3.connect("bot_ratings.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ratings (id_meeting, rate) VALUES (?, ?)", (id_meeting, rate))
    conn.commit()
    conn.close()
