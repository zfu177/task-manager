# Define left Frame elements
from tkinter import *

def onselect(event):
    # Note here that Tkinter passes an event object to onselect()

    w = event.widget
    print(w)

    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))


# https://stackoverflow.com/questions/24656138/python-tkinter-attach-scrollbar-to-listbox-as-opposed-to-window
def create_left_elements(left_frame):

  taskList = Listbox(left_frame, selectmode=SINGLE, height=30)
  taskList.pack(side=LEFT, fill=BOTH)

  scrollbar = Scrollbar(left_frame, orient=VERTICAL)
  scrollbar.config(command=taskList.yview)
  scrollbar.pack(side=RIGHT, fill=BOTH)

  taskList.config(yscrollcommand=scrollbar.set)


  for line in range(100):
    taskList.insert(END, "This is line number " + str(line))


  taskList.bind('<<ListboxSelect>>', onselect)
  # https://www.tutorialspoint.com/python/tk_button.htm
  # Button(left_frame, text="Add Task").grid(row=1, column=0)