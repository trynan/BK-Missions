# GUI testing
# widgets to use:
# Text (used to display text in multiple lines)
# Checkbutton (display options as checkboxes)?
# Buttons
# https://www.tutorialspoint.com/python3/python_gui_programming.htm

from tkinter import *
import random

class Mission:
    def __init__(self, codes, num, name):
        self.codes = codes
        self.num = num
        self.name = name

missions = [
    Mission(["H", "A"],         "2. Side Quest", "{} HCs".format(random.randint(14,18))),
    Mission(["T"],              "2. Side Quest", "All 5 transformations"),
    Mission([],                 "2. Side Quest", "All 10 Brentilda visits"),
    Mission(["O"],              "2. Side Quest", "All 9 orange Jinjos"),
    Mission(["O"],              "2. Side Quest", "All 9 blue Jinjos"),
    Mission(["O"],              "2. Side Quest", "All 9 green Jinjos"),
    Mission(["O"],              "2. Side Quest", "All 9 pink Jinjos"),
    Mission(["O"],              "2. Side Quest", "All 9 yellow Jinjos"),
    Mission(["N"],              "2. Side Quest", "Open the 640 note door"),
    Mission(["T"],              "2. Side Quest", "{} tokens".format(random.randint(70,90))),
    Mission(["J"],              "2. Side Quest", "{} jiggies".format(random.randint(40,55))),
    Mission([],                 "2. Side Quest", "All 3 Cheato Visits"),
    Mission(["J"],              "2. Side Quest", "2 jiggies from each world"),
    Mission(["J"],              "2. Side Quest", "All lair jiggies"),
    Mission([],                 "2. Side Quest", "Activate all 8 warp cauldrons (not Dingpot)"),
    Mission(["R"],              "2. Side Quest", "No RBA"),
    Mission(["R"],              "2. Side Quest", "No FFM"),
    Mission(["R", "J"],         "2. Side Quest", "No MMM early"),
    Mission(["R", "J"],         "2. Side Quest", "No FP early"),
]

used_codes = []
used_codes2 = []

def main():
    done = False
    while not done:
        rn = random.randint(0, len(missions) - 1)
        mission = missions[rn]
        exists = False
        for c in mission.codes:
            if c in used_codes:
                exists = True
                break
        if exists: continue
        done = True
    
    for c in mission.codes:
        # if c in used_codes:
        #     used_codes2.append(c)
        # else:
        used_codes.append(c)
    return mission.name



window = Tk()
def create_buttons():
    b = 0
    for i in range(3):
        for j in range(3):
            b += 1
            Button(window, text = main(), padx = 5, pady = 5).grid(row = i, column = j+2)


# generate board
generate_board = Button(window, text = "Generate Board", command=create_buttons)
generate_board.grid(row = 1, column = 0)

# quit button
quitbutton = Button(window, text = "Quit", command=window.destroy)
quitbutton.grid(row = 2, column = 0)

window.title("Bingo Board")
window.minsize(200,100)

window.mainloop()