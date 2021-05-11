#!/bin/python3

from tkinter import *

tk = Tk()

button1 = Button(tk, text="Button 1")
button1.grid(row=0, column=0)
button2 = Button(tk, text="Button 2")
button2.grid(row=1, column=1, width=10, height=4)


button1.pack()
button2.pack()


tk.mainloop()


