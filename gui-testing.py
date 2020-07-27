# GUI testing
# widgets to use:
# Text (used to display text in multiple lines)
# Checkbutton (display options as checkboxes)?
# Buttons

import tkinter as tk

def main_func():
    print(short.get())

window = tk.Tk()
short = tk.IntVar()
check1 = tk.Checkbutton(text = "short (if not checked, will be long)", variable=short)
check1.pack()
finalbutton = tk.Button(text = "click to generate", command=main_func)
finalbutton.pack()
quitbutton = tk.Button(text = "QUIT", command=window.destroy)
quitbutton.pack()

window.title("lol sup")
window.minsize(200,100)
window.mainloop()