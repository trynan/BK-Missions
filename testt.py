from tkinter import *


win = Tk()
a = IntVar(value = 20)
b = IntVar(value = 15)

intlist = [a, b]

print(intlist[0].get(), intlist[1].get())

a.set(6)
b.set(25)

print(intlist[0].get(), intlist[1].get())