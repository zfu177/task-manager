from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox 
from tkinter import scrolledtext 
from functools import partial
from connection import updateTask, addTask
import calendar


def validate_date(dueDate):
  s = dueDate.split("-")
  if len(s) != 3:
    return False
  
  # Year must be 4 digits
  if len(s[0]) != 4:
    return False
  
  # Month cannot > 12
  if len(s[1]) != 2 or int(s[1]) > 12:
    return False

  # Day cannot > than calendar days range
  if len(s[2]) != 2 or int(s[2]) > calendar.monthrange(int(s[0]), int(s[1]))[1]:
    return False
  
  return True


def clear_contents():
  name_entry.delete(0, END)
  name_entry.insert(0, "")
  date_entry.delete(0, END)
  date_entry.insert(0, "")
  description.delete(1.0, END)
  description.insert(END, "")


def update_fields(data, displayData, tree):
  name_entry.delete(0, END)
  name_entry.insert(0, data[1])

  date_entry.delete(0, END)
  date_entry.insert(0, data[3])

  match data[2]:
    case "high":
      high.invoke()
    case "medium":
      medium.invoke()
    case "low":
      low.invoke()

  description.delete(1.0, END)
  description.insert(END, data[4])

  # https://stackoverflow.com/a/22290388
  action_with_arg = partial(save_task, data[0], displayData, tree)
  save_button.configure(command=action_with_arg)


def save_task(id, displayData, tree):
  task_name = name_entry.get()
  due_date = date_entry.get()
  priority_value = priority_var.get()
  description_value = description.get("1.0", END)

  if task_name == "":
    messagebox.showerror("showerror", "Name cannot be empty")
    return
  elif priority_value == "":
    messagebox.showerror("showerror", "Please select priority")
    return
  elif due_date == "":
    messagebox.showerror("showerror", "Due Date cannot be empty")
    return
  elif validate_date(due_date) is False:
    # Validate date format
    messagebox.showerror("showerror", "Invalid Date Format. Format must be YYYY-MM-DD. Example: 2023-10-10")
    return
  else:
    if id is None:
      # Handle case when "Add Task" button is not clicked and nothing is selected
      new_id, _ = addTask()
      id = new_id

    new_Task = (id, task_name, priority_value, due_date, description_value)
    
    updateTask(new_Task)
    displayData()

    # Auto select the just created task
    children = tree.get_children()
    for child in children:
      item = tree.item(child)
      record = item['values']
      if record[0] == id:
        tree.selection_add(child)
        break

    messagebox.showinfo("showinfo", "Success")
    

def create_right_elements(task_frame, displayData, tree):
  # Name field
  # sticky="W" -- keep west - left
  # https://stackoverflow.com/questions/30550774/how-to-left-justify-python-tkinter-grid-columns-while-filling-entire-cell
  global name_entry, high, low, medium, date_entry, description, save_button, priority_var

  name_label = Label(task_frame, text="Name")
  name_entry = Entry(task_frame)

  name_label.grid(row=0, column=0, padx=10, pady=5, sticky = W)
  name_entry.grid(row=0, column=1, columnspan=6, padx=10, pady=5, sticky=N+S+E+W)

  # Priority field
  priority_label = Label(task_frame, text="Priority")

  priority_var = StringVar()
  
  high = Radiobutton(task_frame, text="High", variable=priority_var, value="high")
  medium = Radiobutton(task_frame, text="Medium", variable=priority_var, value="medium")
  low = Radiobutton(task_frame, text="Low", variable=priority_var, value="low")

  priority_label.grid(row=1, column=0, padx=10, pady=5, sticky = W)
  high.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
  medium.grid(row=1, column=3, columnspan=2, padx=5, pady=5)
  low.grid(row=1, column=5, columnspan=2, padx=5, pady=5)

  # Due Date field
  due_date_label = Label(task_frame, text="Due Date")
  due_date_label.grid(row=2, column=0, padx=10, pady=5, sticky = W)

  date_entry = Entry(task_frame)
  date_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky=N+S+E+W)

  due_date_format_label = Label(task_frame, text="Format: YYYY-MM-DD")
  due_date_format_label.grid(row=2, column=4, columnspan=3, padx=10, pady=5, sticky = W)

  # Description Field
  desc_label = Label(task_frame, text="Description")
  desc_label.grid(row=3, column=0, padx=10, pady=5, sticky = W)
  description = scrolledtext.ScrolledText(task_frame, width=65)
  description.grid(row=3, column=1, columnspan=6, padx=10, pady=5)

  # Save and Clear Button

  action_with_arg = partial(save_task, None, displayData, tree)
  
  save_button = Button(task_frame, text="Save", command=action_with_arg)
  save_button.grid(row=4, column=1, columnspan=3, padx=10, pady=5)
  clear_button = Button(task_frame, text="Clear", command=clear_contents)
  clear_button.grid(row=4, column=4, columnspan=3, padx=10, pady=5)