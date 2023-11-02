import sqlite3
from datetime import date

def Database():
    global conn, cursor
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `tasks` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, priority TEXT, dueDate TEXT, description TEXT)")


def findTasks():
  Database()
  cursor.execute("SELECT * FROM `tasks`")
  tasks = cursor.fetchall()
  cursor.close()
  conn.close()
  return tasks


def findTaskById(id):
  Database()
  cursor.execute("SELECT * FROM `tasks` where id = ?", (str(id),))
  data = cursor.fetchone()
  cursor.close()
  conn.close()
  return data


def addTask():
  Database()
  today = date.today()
  default_task = ("", "low", str(today), "")
  cursor.execute("INSERT INTO `tasks` (name, priority, dueDate, description) VALUES(?, ?, ?, ?)", default_task)
  conn.commit()
  cursor.close()
  conn.close()
  return cursor.lastrowid, default_task



def deleteTaskById(id):
  Database()
  cursor.execute("DELETE FROM `tasks` where id = ?", (str(id),))
  conn.commit()
  cursor.close()
  conn.close()


def deleteAllTasks():
  Database()
  cursor.execute("DELETE FROM `tasks`")
  conn.commit()
  cursor.close()
  conn.close()


def updateTask(data):
  Database()
  cursor.execute("UPDATE `tasks` SET name = ?, priority = ?, dueDate = ?, description = ? where id = ?", (data[1], data[2], data[3], data[4], str(data[0])))
  conn.commit()
  cursor.close()
  conn.close()
