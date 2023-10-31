from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext 
from tkcalendar import DateEntry


def create_right_elements(right_frame):

  # Name field
  # sticky="W" -- keep west - left
  # https://stackoverflow.com/questions/30550774/how-to-left-justify-python-tkinter-grid-columns-while-filling-entire-cell

  name_label = Label(right_frame, text="Name")
  name_entry = Entry(right_frame, width=50)

  name_label.grid(row=0, column=0, padx=10, pady=5, sticky = W)
  name_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5)

  # Priority field
  priority_label = Label(right_frame, text="Priority")

  def print_sel():
    print(priority_var.get())
  
  priority_var = StringVar()

  high = Radiobutton(right_frame, text="High", variable=priority_var, value="high", command=print_sel)
  medium = Radiobutton(right_frame, text="Medium", variable=priority_var, value="medium", command=print_sel)
  low = Radiobutton(right_frame, text="Low", variable=priority_var, value="low", command=print_sel)

  priority_label.grid(row=1, column=0, padx=10, pady=5, sticky = W)
  high.grid(row=1, column=1, padx=10, pady=5)
  medium.grid(row=1, column=2, padx=10, pady=5)
  low.grid(row=1, column=3, padx=10, pady=5)

  # Due Date field
  due_date_label = Label(right_frame, text="Due Date")
  due_date_label.grid(row=2, column=0, padx=10, pady=5, sticky = W)


  #Create a Calendar
  cal = DateEntry(right_frame, selectmode='day', locale='en_US', width=49)
  cal.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

  # Description Field
  desc_label = Label(right_frame, text="Description", justify="left")
  desc_label.grid(row=3, column=0, padx=10, pady=5, sticky = W)
  description = scrolledtext.ScrolledText(right_frame, width=65)
  description.grid(row=3, column=1, columnspan=3, padx=10, pady=5)