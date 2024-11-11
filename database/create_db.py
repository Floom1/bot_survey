import sqlite3

def create_database():
    conn = sqlite3.connect("bot_ratings.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            id_meeting INTEGER PRIMARY KEY,  -- Уникальный ID встречи
            rate INTEGER CHECK(rate >= 1 AND rate <= 10)  -- Оценка от 1 до 10
        )
    ''')
    conn.commit()
    conn.close()

create_database()