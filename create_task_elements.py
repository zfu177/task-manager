from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox 
from tkinter import scrolledtext 
from tkcalendar import DateEntry
from functools import partial
from connection import updateTask


def clear_contents():
  name_entry.delete(0, END)
  name_entry.insert(0, "")
  description.delete(1.0, END)
  description.insert(END, "")


def update_fields(data):
  name_entry.delete(0, END)
  name_entry.insert(0, data[1])

  match data[2]:
    case "high":
      high.invoke()
    case "medimu":
      medium.invoke()
    case "low":
      low.invoke()

  date_picker.set_date(data[3])
  description.delete(1.0, END)
  description.insert(END, data[4])

  # https://stackoverflow.com/a/22290388
  action_with_arg = partial(save_task, data[0])
  save_button.configure(command=action_with_arg)


def save_task(id):
  task_name = name_entry.get()
  due_date = str(date_picker.get_date())
  priority_value = priority_var.get()
  description_value = description.get("1.0", END)
  new_Task = (id, task_name, priority_value, due_date, description_value)
  print(new_Task)

  if task_name == "":
    messagebox.showerror("showerror", "Name cannot be empty")
  else:
    updateTask(new_Task)
    messagebox.showinfo("showinfo", "Success")
    


def create_task_elements(task_frame):
  # Name field
  # sticky="W" -- keep west - left
  # https://stackoverflow.com/questions/30550774/how-to-left-justify-python-tkinter-grid-columns-while-filling-entire-cell

  global name_entry, high, low, medium, date_picker, description, save_button, priority_var

  name_label = Label(task_frame, text="Name")
  name_entry = Entry(task_frame, width=50)

  name_label.grid(row=0, column=0, padx=10, pady=5, sticky = W)
  name_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5)

  # Priority field
  priority_label = Label(task_frame, text="Priority")

  # def print_sel():
  #   print(priority_var.get())
  
  priority_var = StringVar()
  
  high = Radiobutton(task_frame, text="High", variable=priority_var, value="high")
  medium = Radiobutton(task_frame, text="Medium", variable=priority_var, value="medium")
  low = Radiobutton(task_frame, text="Low", variable=priority_var, value="low")

  priority_label.grid(row=1, column=0, padx=10, pady=5, sticky = W)
  high.grid(row=1, column=1, padx=10, pady=5)
  medium.grid(row=1, column=2, padx=10, pady=5)
  low.grid(row=1, column=3, padx=10, pady=5)

  # Due Date field
  due_date_label = Label(task_frame, text="Due Date")
  due_date_label.grid(row=2, column=0, padx=10, pady=5, sticky = W)

  #Create a Calendar
  date_picker = DateEntry(task_frame, selectmode='day', date_pattern='yyyy-MM-dd', locale='en_US', width=49, state="readonly")
  date_picker.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

  # Description Field
  desc_label = Label(task_frame, text="Description", justify="left")
  desc_label.grid(row=3, column=0, padx=10, pady=5, sticky = W)
  description = scrolledtext.ScrolledText(task_frame, width=65)
  description.grid(row=3, column=1, columnspan=3, padx=10, pady=5)

  # Save and Clear Button
  save_button = Button(task_frame, text="Save", command=save_task)
  save_button.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
  clear_button = Button(task_frame, text="Clear", command=clear_contents)
  clear_button.grid(row=4, column=2, columnspan=2, padx=10, pady=5)