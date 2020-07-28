# BK Missions
# Originally written by Trynan and Wedarobi
# UI version by Trynan
# Maintained by Trynan

import tkinter as tk
from operator import attrgetter
import random

class Mission:
    def __init__(self, codes, num, name):
        self.codes = codes
        self.num = num
        self.name = name

# ------------------------------------------------------
# ----------------- INITIALIZE BUTTONS -----------------
# ------------------------------------------------------
window = tk.Tk()
short = tk.IntVar()
codesvar = tk.IntVar()

# short checkbox
short_check = tk.Checkbutton(window)
short_check.grid(row = 0, column = 0)

# codes checkbox
codes_check = tk.Checkbutton(window)
codes_check.grid(row = 1, column = 0)

# main button
main_button = tk.Button(window)
main_button.grid(row = 2, column = 0)

# quit button
quitbutton = tk.Button(window)
quitbutton.grid(row = 3, column = 0, pady=10)

# vertical scroll bar
vscrollb = tk.Scrollbar(window)
vscrollb.grid(row = 0, column = 2, sticky='nsew', rowspan = 5)

# text
text = tk.Text(window)
text['yscrollcommand'] = vscrollb.set
text.grid(row = 0, column = 1, sticky='nsew', rowspan = 5)


# ------------------------------------------------------
# ----------------- HELPER FUNCTION(s) -----------------
# ------------------------------------------------------
def write_text(g, c, s):
    """ g is a list of missions (objects), sorted. c is codesvar (int). 
        s is bool for short. true means short. 
        function writes text to text widget called text """

    text.config(state = tk.NORMAL)
    text.delete("1.0", tk.END)
    text.insert(tk.END, "Initially written by Trynan and Wedarobi\nUI created by Trynan\n\n")
    if not s:
        text.insert(tk.END, "[[BK Missions - LONG]]\n\n")
    else: 
        text.insert(tk.END, "[[BK Missions - SHORT]]\n\n")
    for x in g:
        text.insert(tk.END, x.num)
        text.insert(tk.END, ': ')
        text.insert(tk.END, x.name)
        if c == 1:
            text.insert(tk.END, ' -- ')
            text.insert(tk.END, ', '.join(x.codes))
        text.insert(tk.END, '\n')
    text.config(state = tk.NORMAL)

# ------------------------------------------------------
# ----------------- MAIN FUNCTION HERE -----------------
# ------------------------------------------------------
def main():
    """ main function, gets a set of missions randomly
        based on certain restricitons """
    global short
    if short.get() == 0:
# ----------------- LONG MISSION LIST -----------------
        missions = [
            [ # MAIN_OBJECTIVE
                Mission(["N"],              "1. Main Objective", "Open 765 note door"),
                Mission(["O"],              "1. Main Objective", "All Jinjos"),
                Mission(["N"],              "1. Main Objective", "Defeat Grunty"),
                Mission(["H", "T"],         "1. Main Objective", "All 24 honeycombs"),
                Mission(["T"],              "1. Main Objective", "All 116 tokens"),
                Mission(["J"],              "1. Main Objective", "Open all 9 worlds"),
                Mission(["N", "R"],         "1. Main Objective", "All notes"),
                Mission(["J", "R"],         "1. Main Objective", "{} jiggies".format(random.randint(80,90))),
                Mission(["N", "J", "R"],    "1. Main Objective", "Open DoG & defeat Grunty"),
                Mission(["J"],              "1. Main Objective", "Humanitarian: Chimpy, Blubber, raise Clanker/fix teeth, Tanktup, presents, Gobi's rock, Trunker, Snorkel, Nabnut, Eyrie, Gnawty, Tooty"),
                Mission(["N", "R"],         "1. Main Objective", "Open All 12 Note Doors and Defeat Grunty"),
                Mission(["A"],              "1. Main Objective", "All of 1 type of collectible from each world (all tokens, honeycombs, notes, or jiggies)"),
                # Mission([],      "1. Main Objective", ""),
            ],
            [ # SIDE_QUEST
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
                # Mission([],      "2. Side Quest", ""),
            ],
            [ # EARLY_GAME
                Mission(["O", "A"],         "3. Early Game", "All Jinjos in CC"),
                Mission(["O", "A"],         "3. Early Game", "All Jinjos in FP"),
                Mission(["J", "A"],         "3. Early Game", "{} jiggies in TTC".format(random.randint(8,10))),
                Mission(["J", "A"],         "3. Early Game", "{} jiggies in CC".format(random.randint(8,10))),
                Mission(["N", "A"],         "3. Early Game", "{} notes in CC".format(random.randint(75,100))),
                Mission(["N", "A"],         "3. Early Game", "{} notes in FP".format(random.randint(75,100))),
                Mission(["H", "A"],         "3. Early Game", "Both HCs in TTC"),
                Mission(["H", "A"],         "3. Early Game", "Both HCs in CC"),
                Mission(["H", "A"],         "3. Early Game", "Both HCs in FP"),
                Mission(["T", "A"],         "3. Early Game", "All tokens in TTC"),
                Mission(["J"],              "3. Early Game", "All 4 jiggies inside Clanker"),
                Mission(["R"],              "3. Early Game", "Begin run w/ MM 100% Trotless"),
                Mission(["T", "A"],         "3. Early Game", "All tokens in FP"),
                Mission(["J"],              "3. Early Game", "Merry Christmas! (Visit Boggy's Igloo w/ him in it & give presents)"),
                Mission(["J", "A"],         "3. Early Game", "{} jiggies in FP".format(random.randint(4,9))),
                Mission(["J", "R"],         "3. Early Game", "No jiggies in MM"),
                Mission(["J", "T"],         "3. Early Game", "Termite's Quest: 8 jiggies, 90 notes, & 1 HC as the termite"),
                # Mission([],      "3. Early Game", ""),
            ],
            [ # MID_GAME
                Mission(["O", "A"],         "4. Mid Game", "All Jinjos in MMM"),
                Mission(["O", "A"],         "4. Mid Game", "All Jinjos in GV"),
                Mission(["O", "A"],         "4. Mid Game", "All Jinjos in RBB"),
                Mission(["J", "A"],         "4. Mid Game", "{} jiggies in MMM".format(random.randint(5,10))),
                Mission(["J", "A"],         "4. Mid Game", "{} jiggies in RBB".format(random.randint(3,10))),
                Mission(["N", "A"],         "4. Mid Game", "{} notes in MMM".format(random.randint(50,100))),
                Mission(["N", "A"],         "4. Mid Game", "{} notes in GV".format(random.randint(40,100))),
                Mission(["N", "A"],         "4. Mid Game", "{} notes in RBB".format(random.randint(40,100))),
                Mission(["H", "A"],         "4. Mid Game", "Both HCs in MMM"),
                Mission(["H", "A"],         "4. Mid Game", "Both HCs in GV"),
                Mission(["H", "A"],         "4. Mid Game", "Both HCs in RBB"),
                Mission(["T", "A"],         "4. Mid Game", "{} tokens in MMM".format(random.randint(10,16))),
                Mission(["T", "A"],         "4. Mid Game", "All tokens in GV"),
                Mission(["T", "A"],         "4. Mid Game", "{} tokens in RBB".format(random.randint(10,15))),
                Mission([],                 "4. Mid Game", "MMM witch switch jiggy"),
                Mission([],                 "4. Mid Game", "Kill all 10 Limbos (skeletons) in MMM"),
                Mission([],                 "4. Mid Game", "GV rings jiggy without flight or bee"),
                Mission(["J"],              "4. Mid Game", "Abuse Gobi (beak bust Gobi at all 5 locations)"),
                Mission(["J", "A"],         "4. Mid Game", "{} jiggies in GV".format(random.randint(3,9))),
                # Mission([],      "4. Mid Game", ""),
            ],
            [ # LATE_GAME
                Mission(["O", "A"],         "5. Late Game", "All Jinjos in CCW"),
                Mission(["O", "A"],         "5. Late Game", "All Jinjos in BGS"),
                Mission(["N", "A"],         "5. Late Game", "{} notes in BGS".format(random.randint(50,100))),
                Mission(["H", "A"],         "5. Late Game", "Both HCs in BGS"),
                Mission(["H", "A"],         "5. Late Game", "Both HCs in CCW"),
                Mission(["T", "A"],         "5. Late Game", "All tokens in BGS"),
                Mission(["J"],              "5. Late Game", "Croctuses jiggy"),
                Mission(["J"],              "5. Late Game", "Tiptup's jiggy"),
                Mission(["J"],              "5. Late Game", "Both timed jiggies in BGS"),
                Mission([],                 "5. Late Game", "All caterpillars"),
                Mission(["J"],              "5. Late Game", "Eyrie's Jiggy"),
                Mission(["J"],              "5. Late Game", "Nabnut's Jiggy"),
                Mission([],                 "5. Late Game", "Kill all 5 Sir Slushes in winter"),
                Mission(["J"],              "5. Late Game", "Flower jiggy in CCW"),
                Mission(["N", "A"],         "5. Late Game", "{} notes in CCW".format(random.randint(30,80))),
                Mission(["J", "A"],         "5. Late Game", "{} jiggies in CCW".format(random.randint(3,8))),
                Mission(["J"],              "5. Late Game", "{} jiggies in BGS".format(random.randint(5,8))),
                Mission(["T", "A"],         "5. Late Game", "{} tokens in CCW".format(random.randint(15,25))),
                Mission(["J", "T", "R"],    "5. Late Game", "Collect 10 jiggies as the bee"),
                # Mission([],      "5. Late Game", ""),
            ]
        ]

# ----------------- LONG MISSION GENERATION -----------------
        goals = []
        codes1 = []
        codes2 = []
        codes3 = []
        i_list = []

        for i in range(len(missions)):
            if i == 0:
                # do main objective before all else
                count = len(missions[i])
                rn = random.randint(0, count-1)
                mission = missions[i][rn]
                for c in mission.codes:
                    codes1.append(c)
                goals.append(mission)

            elif i != 0:
                # after i = 0 do them randomly
                rand_i = random.randint(1,len(missions)-1)
                while rand_i in i_list:
                    rand_i = random.randint(1,len(missions)-1)
                i_list.append(rand_i)
                count = len(missions[rand_i])
                
                # get random mission
                done = False
                while not done:
                    rn = random.randint(0, count-1)
                    mission = missions[rand_i][rn]
                    exists = False
                    for c in mission.codes:
                        if c in codes1 or c in codes3:
                            exists = True
                            break
                    if exists: continue
                    done = True
                # add mission's codes to list of codes
                for c in mission.codes:
                    if c in codes2:
                        codes3.append(c)
                    else:
                        codes2.append(c)
                
                goals.append(mission)
            goals_sort = sorted(goals, key=attrgetter('num'))
            # write the sorted goals to the text box widget
            write_text(goals_sort, codesvar.get(), False)


    elif short.get() == 1:
# ----------------- SHORT MISSION LIST -----------------
        missions = [
            [ # MAIN_OBJECTIVE
                Mission(["H"],              "1. Main Objective", "18 HCs"),
                Mission(["T"],              "1. Main Objective", "All 5 tranformations"),
                Mission(["O"],              "1. Main Objective", "All Jinjos of any 1 color (your choice)"),
                Mission([],                 "1. Main Objective", "All 10 Brentilda visits"),
                Mission(["N"],              "1. Main Objective", "Open the 640 note door"),
                Mission(["T"],              "1. Main Objective", "{} tokens".format(random.randint(70,90))),
                Mission(["J"],              "1. Main Objective", "{} jiggies".format(random.randint(40,55))),
                Mission([],                 "1. Main Objective", "All 3 Cheato visits"),
                Mission([],                 "1. Main Objective", "Activate all 8 warp cauldrons (not Dingpot)"),
                Mission(["T"],              "1. Main Objective", "Save Tooty"),
                Mission(["J"],              "1. Main Objective", "2 jiggies from each world"),
                Mission(["J"],              "1. Main Objective", "All lair jiggies"),
            ],
            [ # EARLY_GAME
                Mission(["O", "A"],         "2. Early Game", "All Jinjos in CC"),
                Mission(["O", "A"],         "2. Early Game", "All Jinjos in FP"),
                Mission(["J", "A"],         "2. Early Game", "{} jiggies in TTC".format(random.randint(8,10))),
                Mission(["J", "A"],         "2. Early Game", "{} jiggies in CC".format(random.randint(8,10))),
                Mission(["N", "A"],         "2. Early Game", "{} notes in CC".format(random.randint(75,100))),
                Mission(["N", "A"],         "2. Early Game", "{} notes in FP".format(random.randint(75,100))),
                Mission(["H", "A"],         "2. Early Game", "Both HCs in TTC"),
                Mission(["H", "A"],         "2. Early Game", "Both HCs in CC"),
                Mission(["H", "A"],         "2. Early Game", "Both HCs in FP"),
                Mission(["T", "A"],         "2. Early Game", "All tokens in TTC"),
                Mission(["J"],              "2. Early Game", "All 4 jiggies inside clanker"),
                Mission(["R"],              "2. Early Game", "Begin run w/ MM 100% Trotless"),
                Mission(["T", "A"],         "2. Early Game", "All tokens in FP"),
                Mission(["J"],              "2. Early Game", "Merry Christmas! (Visit Boggy's igloo w/ him in it & give presents)"),
                Mission(["J", "A"],         "2. Early Game", "{} jiggies in FP".format(random.randint(4,9))),
                Mission(["J", "R"],         "2. Early Game", "No jiggies in MM"),
                Mission(["J", "T"],         "2. Early Game", "Termite's Quest: 8 jiggies, 90 notes, & 1 HC as the termite"),
                Mission(["O", "A"],         "2. Early Game", "All Jinjos in MMM"),
                Mission(["J", "A"],         "2. Early Game", "{} jiggies in MMM".format(random.randint(5,10))),
                Mission(["N", "A"],         "2. Early Game", "{} notes in MMM".format(random.randint(50,100))),
                Mission(["H", "A"],         "2. Early Game", "Both HCs in MMM"),
                Mission(["T", "A"],         "2. Early Game", "{} tokens in MMM".format(random.randint(10,16))),
                Mission([],                 "2. Early Game", "MMM witch switch jiggy"),
                Mission([],                 "2. Early Game", "Kill all 10 Limbos (skeletons) in MMM"),
            ],
            [ # LATE_GAME
                Mission(["O", "A"],         "3. Late Game", "All Jinjos in GV"),
                Mission(["N", "A"],         "3. Late Game", "{} notes in GV".format(random.randint(40,100))),
                Mission(["H", "A"],         "3. Late Game", "Both HCs in GV"),
                Mission(["T", "A"],         "3. Late Game", "All tokens in GV"),
                Mission([],                 "3. Late Game", "GV rings jiggy without flight or bee"),
                Mission(["J", "A"],         "3. Late Game", "{} jiggies in GV".format(random.randint(3,9))),
                Mission(["J"],              "3. Late Game", "Abuse Gobi (beak bust Gobi at all 5 locations)"),
                Mission(["O", "A"],         "3. Late Game", "All Jinjos in RBB"),
                Mission(["J", "A"],         "3. Late Game", "{} jiggies in RBB".format(random.randint(3,10))),
                Mission(["N", "A"],         "3. Late Game", "{} notes in RBB".format(random.randint(40,100))),
                Mission(["H", "A"],         "3. Late Game", "Both HCs in RBB"),
                Mission(["T", "A"],         "3. Late Game", "{} tokens in RBB".format(random.randint(10,15))),
                Mission(["O", "A"],         "3. Late Game", "All Jinjos in CCW"),
                Mission(["O", "A"],         "3. Late Game", "All Jinjos in BGS"),
                Mission(["N", "A"],         "3. Late Game", "{} notes in BGS".format(random.randint(50,100))),
                Mission(["H", "A"],         "3. Late Game", "Both HCs in BGS"),
                Mission(["H", "A"],         "3. Late Game", "Both HCs in CCW"),
                Mission(["T", "A"],         "3. Late Game", "All tokens in BGS"),
                Mission(["J"],              "3. Late Game", "Croctuses jiggy"),
                Mission(["J"],              "3. Late Game", "Tiptup's jiggy"),
                Mission(["J"],              "3. Late Game", "Both timed jiggies in BGS"),
                Mission([],                 "3. Late Game", "All caterpillars"),
                Mission(["J"],              "3. Late Game", "Eyrie's jiggy"),
                Mission(["J"],              "3. Late Game", "Nabnut's jiggy"),
                Mission([],                 "3. Late Game", "Kill all 5 Sir Slushes in winter"),
                Mission(["J"],              "3. Late Game", "Flower jiggy in CCW"),
                Mission(["N", "A"],         "3. Late Game", "{} notes in CCW".format(random.randint(30,80))),
                Mission(["J", "A"],         "3. Late Game", "{} jiggies in CCW".format(random.randint(3,8))),
                Mission(["J"],              "3. Late Game", "{} jiggies in BGS".format(random.randint(5,9))),
                Mission(["T", "A"],         "3. Late Game", "{} tokens in CCW".format(random.randint(15,25))),
                Mission(["J", "T", "R"],    "3. Late Game", "Collect 10 jiggies as the bee"),
            ]
        ]

# ----------------- SHORT MISSION GENERATION -----------------
        goals = []
        codes = []
        i_list = []

        for i in range(len(missions)):
            if i == 0:
                # do main objective before all else
                count = len(missions[i])
                rn = random.randint(0, count-1)
                mission = missions[i][rn]
                for c in mission.codes:
                    codes.append(c)
                goals.append(mission)

            elif i != 0:
                # after i = 0 do them randomly
                rand_i = random.randint(1,len(missions)-1)
                while rand_i in i_list:
                    rand_i = random.randint(1,len(missions)-1)
                i_list.append(rand_i)
                count = len(missions[rand_i])

                # get random mission
                done = False
                while not done:
                    rn = random.randint(0, count-1)
                    mission = missions[rand_i][rn]
                    exists = False
                    for c in mission.codes:
                        if c in codes:
                            exists = True
                            break
                    if exists: continue
                    done = True

                # comment this code below to enable/disable repeating codes for early/late game
                # if it's commented out that means codes can repeat for 2/3 (as long as they don't share 1's goal)
                # vvvvvvvvvvvvvvvvvvvvvvv
                for c in mission.codes:
                    codes.append(c)
                # ^^^^^^^^^^^^^^^^^^^^^^^
            
                goals.append(mission)
            goals_sort = sorted(goals, key=attrgetter('num'))
            # write the sorted goals to the text box widget
            write_text(goals_sort, codesvar.get(), True)


# --------------------------------------------------
# ----------------- CONFIG BUTTONS -----------------
# --------------------------------------------------
short_check.config(\
    text = "Short (if checked, short\nboard will be generated)", \
    variable = short)

codes_check.config(\
    text = "Show codes after each goal", \
    variable = codesvar)

main_button.config(\
    text = "Click to generate missions!", \
    command = main)

quitbutton.config(\
    text = "Quit", \
    command = window.destroy)

text.config(\
    state = tk.DISABLED, \
    height = 13, \
    width = 70)

vscrollb.config(\
    command = text.yview)

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

window.title("BK Missions Generator")
window.minsize(500,120)
window.maxsize(1000,300)
window.mainloop()