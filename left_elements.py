# Define left Frame elements
from tkinter import *
import tkinter.ttk as ttk
import connection

def insertData():
  connection.Database()
  connection.cursor.execute("INSERT INTO `tasks` (name, priority, dueDate, description) VALUES(?, ?, ?, ?)", ("test", "high", "2023-10-13", "no desc"))
  connection.conn.commit()
  connection.cursor.close()
  connection.conn.close()

def displayData(tree):
  tree.delete(*tree.get_children())
  connection.Database()
  connection.cursor.execute("SELECT * FROM `tasks`")
  fetch = connection.cursor.fetchall()
  for data in fetch:
      # Insert only task names
      print(data)
      tree.insert('', 'end', values=(data[0], data[1]))
  connection.cursor.close()
  connection.conn.close()


# https://stackoverflow.com/questions/24656138/python-tkinter-attach-scrollbar-to-listbox-as-opposed-to-window
def create_left_elements(left_frame):

  list_frame = Frame(left_frame)
  bottom_menu_frame = Frame(left_frame)
  
  # ------ Treeview and Scrollbar ------

  scrollbary = Scrollbar(list_frame, orient=VERTICAL)
  tree = ttk.Treeview(list_frame, columns=("id", "name"), selectmode="extended", height=300, yscrollcommand=scrollbary.set)
  scrollbary.config(command=tree.yview)
  scrollbary.pack(side=RIGHT, fill=Y)
  tree.heading('id', text="ID", anchor=W)
  tree.column('#0', stretch=NO, minwidth=0, width=0)
  tree.heading('name', text="Name", anchor=W)
  tree.column('#1', stretch=NO, minwidth=0, width=100)
  
  tree.pack()

  # https://www.pythontutorial.net/tkinter/tkinter-treeview/
  def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)


  tree.bind('<<TreeviewSelect>>', item_selected)

  # insertData()

  displayData(tree)

  # for line in range(100):
  #   taskList.insert(END, "This is line number " + str(line))

  # taskList.bind('<<ListboxSelect>>', onselect)
  # ------ Listbox and Scrollbar ------

  # https://www.tutorialspoint.com/python/tk_button.htm
  add_task_btn = Button(bottom_menu_frame, text="Add Task")

  list_frame.pack(fill=BOTH, side=TOP)
  bottom_menu_frame.pack(fill=X, side=BOTTOM)
  add_task_btn.pack(side=LEFT)
