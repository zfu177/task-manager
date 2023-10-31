from tkinter import *
from left_elements import create_left_elements
from right_elements import create_right_elements

root = Tk()  # create a root widget
root.title("Task Management Application (Zhongyi Fu)")
root.configure(background="white")
root.minsize(950, 470)  # width, height
root.maxsize(950, 470)
root.geometry("950x470+300+300")  # width x height + x + y

main_frame = Frame(root, width=650, height=650, padx=10, pady=10)
main_frame.pack()

left_frame = Frame(main_frame, width=200, height=600, padx=10, pady=10)
left_frame.pack(side=LEFT)

right_frame = Frame(main_frame, width=400, height=600, padx=10, pady=10)
right_frame.pack(side=RIGHT)

create_left_elements(left_frame)
create_right_elements(right_frame)

root.mainloop()