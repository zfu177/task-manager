from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext 
from tkcalendar import DateEntry

def sel():
   selection = "You selected the option " + str(StringVar.get())
   print(selection)


def create_right_elements(right_frame):

  # Name field
  # sticky="W" -- keep west - left
  # https://stackoverflow.com/questions/30550774/how-to-left-justify-python-tkinter-grid-columns-while-filling-entire-cell

  name_label = Label(right_frame, text="Name")
  name_entry = Entry(right_frame)

  name_label.grid(row=0, column=0, padx=10, pady=5, sticky = W)
  name_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5)

  # Priority field

  priority_label = Label(right_frame, text="Priority")

  high = Radiobutton(right_frame, text="High", variable=StringVar, value="high", command=sel)
  medium = Radiobutton(right_frame, text="Medium", variable=StringVar, value="medium", command=sel)
  low = Radiobutton(right_frame, text="Low", variable=StringVar, value="low", command=sel)

  priority_label.grid(row=1, column=0, padx=10, pady=5, sticky = W)
  high.grid(row=1, column=1, padx=10, pady=5)
  medium.grid(row=1, column=2, padx=10, pady=5)
  low.grid(row=1, column=3, padx=10, pady=5)


  # Due Date field
  due_date_label = Label(right_frame, text="Due Date")
  due_date_label.grid(row=2, column=0, padx=10, pady=5, sticky = W)

  #Create a Calendar using DateEntry
  cal = DateEntry(right_frame, width=26, background='darkblue', foreground='white',  year=2023)
  cal.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

  # Description Field
  desc_label = Label(right_frame, text="Description", justify="left")
  desc_label.grid(row=3, column=0, padx=10, pady=5, sticky = W)
  description = scrolledtext.ScrolledText(right_frame)
  description.grid(row=3, column=1, columnspan=3, padx=10, pady=5)