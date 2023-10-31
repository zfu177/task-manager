from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext 
from tkcalendar import DateEntry

def sel():
   selection = "You selected the option " + str(StringVar.get())
   print(selection)


def create_right_elements(right_frame):
  # Align left
  # https://stackoverflow.com/questions/31140590/how-to-line-left-justify-label-and-entry-boxes-in-tkinter-grid

  # Name field
  Label(right_frame, text="Name", justify="left").grid(row=0, column=0, sticky = W)
  name = Entry(right_frame, width = 26, justify="left")
  name.grid(row=0, column=1, sticky = W)

  # Priority field
  Label(right_frame, text="Priority", justify="left").grid(row=1, column=0, sticky = W)
  # https://www.pythontutorial.net/tkinter/tkinter-combobox/
  # https://stackoverflow.com/questions/44959253/how-can-i-disable-typing-in-a-ttk-combobox-tkinter
  # priority = Combobox(right_frame, state="readonly", width = 26, justify="left") 
  # priority.grid(row=1, column=1, sticky = W)

  high = Radiobutton(right_frame, text="High", variable=StringVar, value="high", command=sel)
  medium = Radiobutton(right_frame, text="Medium", variable=StringVar, value="medium", command=sel)
  low = Radiobutton(right_frame, text="Low", variable=StringVar, value="low", command=sel)

  high.grid(row=1, column=1, sticky = W)
  medium.grid(row=1, column=2, sticky = W)
  low.grid(row=1, column=3, sticky = W)
  


  # Due Date field
  Label(right_frame, text="Due Date", justify="left").grid(row=2, column=0, sticky = W)
  #Create a Calendar using DateEntry
  cal = DateEntry(right_frame, width=26, background='darkblue',
                    foreground='white', borderwidth=2, year=2023, justify="left")
  
  cal.grid(row=2, column=1, sticky="W")

  # Description Field
  Label(right_frame, text="Description", justify="left").grid(row=3, column=0, sticky = W)
  description = scrolledtext.ScrolledText(right_frame, width = 30)
  description.grid(row=3, column=1, sticky = W)