from tkinter import *
from left_elements import create_left_elements
from right_elements import create_right_elements

root = Tk()  # create a root widget
root.title("Task Management Application (Zhongyi Fu)")
root.configure(background="white")
root.minsize(935, 650)  # width, height
root.maxsize(935, 650)
root.geometry("935x650+300+300")  # width x height + x + y

main_frame = Frame(root, width=650, height=650, padx=5, pady=5)
main_frame.pack()

left_frame = Frame(main_frame, width=200, height=640, padx=5)
left_frame.pack(side=LEFT)

right_frame = Frame(main_frame, width=400, height=640, padx=5)
right_frame.pack(side=RIGHT)

displayData, tree = create_left_elements(left_frame)
create_right_elements(right_frame, displayData, tree)

root.mainloop()