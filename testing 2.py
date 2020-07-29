# testing

from tkinter import *

win = Tk()

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
varlist = [c1, c2, c3, c4]

def open_window():
    new_win = Toplevel(win)
    new_win.title("Settings")
    new_quit_button = Button(new_win, text = "exit settings", command = new_win.destroy)
    check1 = Checkbutton(new_win, text = "checkbox 1", variable = c1)
    check2 = Checkbutton(new_win, text = "checkbox 2", variable = c2)
    check3 = Checkbutton(new_win, text = "checkbox 3", variable = c3)
    check4 = Checkbutton(new_win, text = "checkbox 4", variable = c4)
    check1.grid(row = 0, column = 0)
    check2.grid(row = 0, column = 1)
    check3.grid(row = 1, column = 0)
    check4.grid(row = 1, column = 1)
    new_quit_button.grid(row = 2, column = 0, columnspan = 2)
    new_win.geometry("200x100")
    new_win.minsize(200,100)
    new_win.maxsize(500,500)


def do_the_thing():
    global c1, c2, c3, c4
    varlist = [c1.get(), c2.get(), c3.get(), c4.get()]
    text.configure(state = NORMAL)
    text.delete("1.0", END)

    for i, c in enumerate(varlist):
        text.insert(END, "checkbox " + str(i+1) + ": ")
        if c == 1:
            text.insert(END, "checked\n")
        else:
            text.insert(END, "not checked\n")
    text.configure(state = DISABLED)
    


text_button = Button(win, text = "do the thing", command = do_the_thing)
text_button.grid(row = 1, column = 0, pady = 7)

show_settings = Button(win, text = "Show Settings", command = open_window)
show_settings.grid(row = 2, column = 0, padx = 7)

quit_button = Button(win, text = "quit", command = win.destroy)
quit_button.grid(row = 3, column = 0, pady = 7)

text = Text(state = DISABLED, height = 15, width = 400)
text.grid(row = 0, column = 1, sticky='nsew', rowspan = 4)


win.grid_columnconfigure(1, weight = 1)
win.grid_rowconfigure(0, weight = 1)
win.geometry("500x200")
win.minsize(200,200)
win.maxsize(500,500)

win.mainloop()