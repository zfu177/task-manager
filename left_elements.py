# Define left Frame elements
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from right_elements import update_fields, clear_contents
from connection import addTask, findTaskById, findTasks, deleteTaskById, deleteAllTasks


# https://stackoverflow.com/questions/24656138/python-tkinter-attach-scrollbar-to-listbox-as-opposed-to-window
def create_left_elements(left_frame):

  list_frame = Frame(left_frame)
  
  # ------ Treeview and Scrollbar ------
  Label(left_frame, text="My Tasks", font=("Times", 20)).pack(side=TOP, pady=10)

  scrollbary = Scrollbar(list_frame, orient=VERTICAL)
  tree = ttk.Treeview(list_frame, columns=("id", "name"), selectmode="browse", height=30, yscrollcommand=scrollbary.set)
  scrollbary.config(command=tree.yview)
  tree.heading('id', text="ID", anchor=W)
  tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
  tree.heading('name', text="Name", anchor=W)
  tree.column('#1', stretch=NO, minwidth=0, width=100, anchor=CENTER)
  
  scrollbary.pack(side=RIGHT, fill=Y)
  tree.pack(side=LEFT)


  def displayData():
    tree.delete(*tree.get_children())
    fetch = findTasks()
    for data in fetch:
        # Insert only task id and names
        # for each loop, insert at the end
        tree.insert('', 'end', values=(data[0], data[1]))


  # Display data on launch
  displayData()


  # https://www.pythontutorial.net/tkinter/tkinter-treeview/
  def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        data = findTaskById(record[0])
        
        update_fields(data, displayData, tree)

  tree.bind('<<TreeviewSelect>>', item_selected)


  # If data exist, automatically select the first row
  children = tree.get_children()
  if (len(children) > 0):
    tree.selection_add(children[0])
  
  list_frame.pack(side=TOP)

  # https://www.tutorialspoint.com/python/tk_button.htm

  # Add an empty task when clicking the "Add Task" button
  def addEmptyTask():
     addTask()
     displayData()
     children = tree.get_children()
     tree.selection_add(children[-1])

  
  def deleteSelectedTask():
    for selected_item in tree.selection():
      item = tree.item(selected_item)
      record = item['values']
      deleteTaskById(record[0])
      displayData()
      messagebox.showinfo("showinfo", "Success")
      # After delete select the first item if exist
      children = tree.get_children()
      if (len(children) > 0):
        tree.selection_add(children[0])
      else:
         # Otherwise, if no items at all, clear the contents on
         clear_contents()

  def deleteAll():
     confirmed = messagebox.askyesno(title="Confirm Delete All Tasks", message="Are you sure you want to delete all tasks?")
     if confirmed:
      deleteAllTasks()
      clear_contents()
      displayData()
      messagebox.showinfo("showinfo", "Success")


  # Pack elements
  bottom_menu_frame = Frame(left_frame)
  bottom_menu_frame.pack(side=BOTTOM)
  add_task_btn = Button(bottom_menu_frame, text="Add Task", command=addEmptyTask)
  delete_task_btn = Button(bottom_menu_frame, text="Delete Task", command=deleteSelectedTask)
  delete_all_btn = Button(bottom_menu_frame, text="Delete All", command=deleteAll)
  add_task_btn.pack(side=LEFT)
  delete_all_btn.pack(side=RIGHT)
  delete_task_btn.pack(side=RIGHT)

  return displayData, tree
