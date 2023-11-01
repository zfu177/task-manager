# Define left Frame elements
from tkinter import *
from tkinter import messagebox 
import tkinter.ttk as ttk
from create_task_elements import update_fields
from connection import addTask, findTaskById, findTasks, deleteTaskById


def displayData():
  tree.delete(*tree.get_children())
  fetch = findTasks()
  for data in fetch:
      # Insert only task names
      # insert at the end
      tree.insert('', 'end', values=(data[0], data[1]))


# https://stackoverflow.com/questions/24656138/python-tkinter-attach-scrollbar-to-listbox-as-opposed-to-window
def create_left_elements(left_frame):

  list_frame = Frame(left_frame)
  
  # ------ Treeview and Scrollbar ------
  global tree

  Label(left_frame, text="My Tasks", font=("Times", 20)).pack(side=TOP, pady=10)

  scrollbary = Scrollbar(list_frame, orient=VERTICAL)
  tree = ttk.Treeview(list_frame, columns=("id", "name"), selectmode="extended", height=30, yscrollcommand=scrollbary.set)
  scrollbary.config(command=tree.yview)
  tree.heading('id', text="ID", anchor=W)
  tree.column('#0', stretch=NO, minwidth=0, width=0)
  tree.heading('name', text="Name", anchor=W)
  tree.column('#1', stretch=NO, minwidth=0, width=100)
  
  scrollbary.pack(side=RIGHT, fill=Y)
  tree.pack(side=LEFT)

  # https://www.pythontutorial.net/tkinter/tkinter-treeview/
  def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)
        data = findTaskById(record[0])
        update_fields(data)

  tree.bind('<<TreeviewSelect>>', item_selected)

  # insertData()
  displayData()
  

  
  list_frame.pack(side=TOP)

  # https://www.tutorialspoint.com/python/tk_button.htm

  def addEmptyTask():
     id, default_task = addTask()
     displayData()
     update_fields((id, default_task[0], default_task[1], default_task[2], default_task[3]))
     
  
  def deleteSelectedTask():
    for selected_item in tree.selection():
      item = tree.item(selected_item)
      record = item['values']
      deleteTaskById(record[0])
      displayData()
      messagebox.showinfo("showinfo", "Success")


  bottom_menu_frame = Frame(left_frame)
  bottom_menu_frame.pack(side=BOTTOM)
  add_task_btn = Button(bottom_menu_frame, text="Add Task", command=addEmptyTask)
  delete_task_btn = Button(bottom_menu_frame, text="Delete Task", command=deleteSelectedTask)
  add_task_btn.pack(side=LEFT)
  delete_task_btn.pack(side=RIGHT)
