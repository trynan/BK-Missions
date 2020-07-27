# GUI testing
# widgets to use:
# Text (used to display text in multiple lines)
# Checkbutton (display options as checkboxes)?
# Buttons

import tkinter as tk
test = "hello!"

def main():
    text.config(state=tk.NORMAL)
    text.delete("1.0",tk.END)
    if short.get() == 1:
        text.insert(tk.END, "\nthe box is checked!"+test)
    elif short.get() == 0:
        text.insert(tk.END, "\nthe box is not checked.")
    text.config(state=tk.DISABLED)

def clear_text():
    text.config(state=tk.NORMAL)
    text.delete("1.0",tk.END)
    text.config(state=tk.DISABLED)

window = tk.Tk()
short = tk.IntVar()

# checkbox
check1 = tk.Checkbutton(window, text = "short (if not checked, will be long)", variable=short)
check1.grid(row = 0, column = 0)

# checkbox button
checkbox_button = tk.Button(window, text = "click to show checkbox value", \
    command=main)
checkbox_button.grid(row = 1, column = 0)

# clear text button
clearbutton = tk.Button(window, text = "Clear Textbox", command=clear_text)
clearbutton.grid(row = 2, column = 0)

# quit button
quitbutton = tk.Button(window, text = "Quit", command=window.destroy)
quitbutton.grid(row = 3, column = 0)

# scroll bar
scrollb = tk.Scrollbar()
scrollb.grid(row = 0, column = 2, sticky='nsew', rowspan = 4)

# text
text = tk.Text(window, state=tk.DISABLED)
text['yscrollcommand'] = scrollb.set
text.grid(row = 0, column = 1, sticky='nsew', rowspan = 4)

scrollb.config(command = text.yview)

window.title("BK Missions Generator")
window.minsize(200,100)

window.mainloop()