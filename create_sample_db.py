# Simple script to create a sample SQLite DB with the expected Student table
import sqlite3
from datetime import datetime

conn = sqlite3.connect('students.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TEXT
    )
''')
now = datetime.utcnow().isoformat()
samples = [
    ('Ben Attuah', 'ben@example.com', now),
    ('Ama Serwaa', 'ama@example.com', now),
    ('Kojo Mensah', 'kojo@example.com', now)
]
c.executemany('INSERT OR IGNORE INTO student (name,email,created_at) VALUES (?,?,?)', samples)
conn.commit()
conn.close()
print('Created students.db with sample entries (table name: student)')