from tkinter import *
from left_elements import create_left_elements
from right_elements import create_right_elements

root = Tk()  # create a root widget
root.title("Task Management Application (Zhongyi Fu)")
root.configure(background="white")
# root.minsize(200, 200)  # width, height
# root.maxsize(500, 500)
root.geometry("650x650+300+300")  # width x height + x + y


main_frame = Frame(root, width=650, height=650)
main_frame.grid(row=0, column=0)

left_frame = Frame(main_frame, width=200, height=600)
left_frame.grid(row=0, column=0, padx=10, pady=5)

create_left_elements(left_frame)

right_frame = Frame(main_frame, width=400, height=600)
right_frame.grid(row=0, column=1, padx=10, pady=5)
create_right_elements(right_frame)

root.mainloop()