from tkinter import *
from left_elements import create_left_elements
from create_task_elements import create_task_elements

root = Tk()  # create a root widget
root.title("Task Management Application (Zhongyi Fu)")
root.configure(background="white")
root.minsize(950, 700)  # width, height
root.geometry("950x700+300+300")  # width x height + x + y

main_frame = Frame(root, width=650, height=650, padx=10, pady=10)
main_frame.pack()

left_frame = Frame(main_frame, width=200, height=640, padx=10, pady=10)
left_frame.pack(side=LEFT)

right_frame = Frame(main_frame, width=400, height=640, padx=10, pady=10)
right_frame.pack(side=RIGHT)

task_frame = Frame(right_frame)
task_frame.pack(side=TOP)

create_left_elements(left_frame)
create_task_elements(task_frame)

root.mainloop()