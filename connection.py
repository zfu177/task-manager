import sqlite3

def Database():
    global conn, cursor
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `tasks` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, priority TEXT, dueDate TEXT, description TEXT)")
