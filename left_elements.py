# Define left Frame elements
from tkinter import *

def onselect(event):
    # Note here that Tkinter passes an event object to onselect()

    w = event.widget

    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))


# https://stackoverflow.com/questions/24656138/python-tkinter-attach-scrollbar-to-listbox-as-opposed-to-window
def create_left_elements(left_frame):

  list_frame = Frame(left_frame)
  bottom_menu_frame = Frame(left_frame)
  
  # ------ Listbox and Scrollbar ------
  # height 20 rows
  taskList = Listbox(list_frame, selectmode=SINGLE, height=20)

  scrollbar = Scrollbar(list_frame, orient=VERTICAL)
  scrollbar.config(command=taskList.yview)
  taskList.config(yscrollcommand=scrollbar.set)

  taskList.pack(side=LEFT, fill=BOTH)
  scrollbar.pack(side=RIGHT, fill=BOTH)

  for line in range(100):
    taskList.insert(END, "This is line number " + str(line))

  taskList.bind('<<ListboxSelect>>', onselect)
  # ------ Listbox and Scrollbar ------

  # https://www.tutorialspoint.com/python/tk_button.htm
  add_task_btn = Button(bottom_menu_frame, text="Add Task")

  list_frame.pack(fill=BOTH, side=TOP)
  bottom_menu_frame.pack(fill=X, side=BOTTOM)
  add_task_btn.pack(side=LEFT)
