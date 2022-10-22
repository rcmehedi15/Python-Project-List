from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital Watch Developer MD Mehedi Hasan")


def time():
    string = strftime('%H:%H:%S %p')
    Label.config(text=string)
    Label.after(1000,time)

Label = Label(root,font =("Bleeding-Cowboys",80),background="#400D51",foreground="white")

Label.pack(anchor='center')
time()

mainloop()



