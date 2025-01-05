import sqlite3

# データベースとテーブルを作成
conn = sqlite3.connect('ziri.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)
''')

conn.commit()
conn.close()

print("Database and table created!")
