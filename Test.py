from tkinter import *

window = Tk()
window.geometry("300x300")  # for frame sizing
window.title("Welcome")


def exit1():
    exit();


button1 = Button(window, text="burger", relief=RAISED, command=exit1)  # GROOVE, RIDGE, SUNKEN, RAISED
# command = "function" to give button functionality
button1.place(x=60, y=50)

window.mainloop()
