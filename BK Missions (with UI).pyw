# BK Missions
# Originally written by Trynan and Wedarobi
# UI version by Trynan
# Maintained by Trynan

import tkinter as tk
from operator import attrgetter
import random

class Mission:
    def __init__(self, codes, num, name, rand):
        self.codes = codes # list of codes, ie ["N", "A"]
        self.num = num # number of goal, ie "1. Main Objective"
        self.name = name # name of goal, ie "Open 765 note door"
        self.rand = rand # 0 means normal, 1 means random, 2 means normal variant of a random goal

show_missions_var = False

# ------------------------------------------------------
# ----------------- INITIALIZE BUTTONS -----------------
# ------------------------------------------------------
window = tk.Tk()
short = tk.IntVar()
codesvar = tk.IntVar()
randvar = tk.IntVar()

# short checkbox
short_check = tk.Checkbutton(window)
short_check.grid(row = 1, column = 0, pady=10)

# random checkbox
rand_check = tk.Checkbutton(window)
rand_check.grid(row = 2, column = 0, pady=10)

# codes checkbox
codes_check = tk.Checkbutton(window)
codes_check.grid(row = 3, column = 0, pady=10)

# main button
main_button = tk.Button(window)
main_button.grid(row = 4, column = 0, pady=10)

# show missions button
missions_button = tk.Button(window)
missions_button.grid(row = 5, column = 0, pady=10)

# quit button
quit_button = tk.Button(window)
quit_button.grid(row = 6, column = 0, pady=10)

# vertical scroll bar
vscrollb = tk.Scrollbar(window)
vscrollb.grid(row = 0, column = 2, sticky='nsew', rowspan = 14)

# text
text = tk.Text(window)
text['yscrollcommand'] = vscrollb.set
text.grid(row = 0, column = 1, sticky='nsew', rowspan = 14)


# -------------------------------------------------------
# ----------------- WRITE TEXT FUNCTION -----------------
# -------------------------------------------------------
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
    text.config(state = tk.DISABLED)

# ------------------------------------------------------
# ----------------- MAIN FUNCTION HERE -----------------
# ------------------------------------------------------
def main():
    """ main function, gets a set of missions randomly
        based on certain restricitons """
    global short
    global show_missions_var
    global codesvar
    if short.get() == 0:
# ----------------- LONG MISSION LIST -----------------
        missions = [
            [ # MAIN_OBJECTIVE
                Mission(["N"],              "1. Main Objective", "Open 765 note door", 0),
                Mission(["O"],              "1. Main Objective", "All Jinjos", 0),
                Mission(["N"],              "1. Main Objective", "Defeat Grunty", 0),
                Mission(["H", "T"],         "1. Main Objective", "All 24 honeycombs", 0),
                Mission(["T"],              "1. Main Objective", "All 116 tokens", 0),
                Mission(["J"],              "1. Main Objective", "Open all 9 worlds", 0),
                Mission(["N", "R"],         "1. Main Objective", "All notes", 0),
                Mission(["J", "R"],         "1. Main Objective", "{} jiggies [r 80-90]".format(random.randint(80,90)), 1),
                Mission(["J", "R"],         "1. Main Objective", "85 jiggies", 2),
                
                Mission(["N", "J", "R"],    "1. Main Objective", "Open DoG & defeat Grunty", 0),
                Mission(["J"],              "1. Main Objective", "Humanitarian: Jiggies: Chimpy, Blubber, raise Clanker/fix both teeth, Tanktup, presents in FP, Gobi's rock, Trunker, Snorkel, Nabut, Eyrie\n Others (no jiggy): Gnawty's Boulder, Tooty", 0),
                Mission(["N", "R"],         "1. Main Objective", "Open All 12 Note Doors and Defeat Grunty", 0),
                Mission(["A"],              "1. Main Objective", "All of 1 type of collectible from each world (all tokens, honeycombs, notes, or jiggies)", 0),
                # Mission([],      "1. Main Objective", ""),
            ],
            [ # SIDE_QUEST
                Mission(["H", "A"],         "2. Side Quest", "{} HCs [r 14-18]".format(random.randint(14,18)), 1),
                Mission(["H", "A"],         "2. Side Quest", "18 HCs", 2),

                Mission(["T"],              "2. Side Quest", "All 5 transformations", 0),
                Mission([],                 "2. Side Quest", "All 10 Brentilda visits", 0),
                Mission(["O"],              "2. Side Quest", "All 9 orange Jinjos", 0),
                Mission(["O"],              "2. Side Quest", "All 9 blue Jinjos", 0),
                Mission(["O"],              "2. Side Quest", "All 9 green Jinjos", 0),
                Mission(["O"],              "2. Side Quest", "All 9 pink Jinjos", 0),
                Mission(["O"],              "2. Side Quest", "All 9 yellow Jinjos", 0),
                Mission(["N"],              "2. Side Quest", "Open the 640 note door", 0),
                Mission(["T"],              "2. Side Quest", "{} tokens [r 70-90]".format(random.randint(70,90)), 1),
                Mission(["T"],              "2. Side Quest", "90 tokens", 2),

                Mission(["J"],              "2. Side Quest", "{} jiggies [r 40-55]".format(random.randint(40,55)), 1),
                Mission(["J"],              "2. Side Quest", "45 jiggies", 2),

                Mission([],                 "2. Side Quest", "All 3 Cheato Visits", 0),
                Mission(["J"],              "2. Side Quest", "2 jiggies from each world", 0),
                Mission(["J"],              "2. Side Quest", "All lair jiggies", 0),
                Mission([],                 "2. Side Quest", "Activate all 8 warp cauldrons (not Dingpot)", 0),
                Mission(["R"],              "2. Side Quest", "No RBA", 0),
                Mission(["R"],              "2. Side Quest", "No FFM", 0),
                Mission(["R", "J"],         "2. Side Quest", "No MMM early", 0),
                Mission(["R", "J"],         "2. Side Quest", "No FP early", 0),
                # Mission([],      "2. Side Quest", ""),
            ],
            [ # EARLY_GAME
                Mission(["O", "A"],         "3. Early Game", "All Jinjos in CC", 0),
                Mission(["O", "A"],         "3. Early Game", "All Jinjos in FP", 0),
                Mission(["J", "A"],         "3. Early Game", "{} jiggies in TTC [r 8-10]".format(random.randint(8,10)), 1),
                Mission(["J", "A"],         "3. Early Game", "All jiggies in TTC", 2),

                Mission(["J", "A"],         "3. Early Game", "{} jiggies in CC [r 8-10]".format(random.randint(8,10)), 1),
                Mission(["J", "A"],         "3. Early Game", "All jiggies in CC", 2),

                Mission(["N", "A"],         "3. Early Game", "{} notes in CC [r 75-100]".format(random.randint(75,100)), 1),
                Mission(["N", "A"],         "3. Early Game", "All notes in CC", 2),

                Mission(["N", "A"],         "3. Early Game", "{} notes in FP [r 75-100]".format(random.randint(75,100)), 1),
                Mission(["N", "A"],         "3. Early Game", "All notes in FP", 2),

                Mission(["H", "A"],         "3. Early Game", "Both HCs in TTC", 0),
                Mission(["H", "A"],         "3. Early Game", "Both HCs in CC", 0),
                Mission(["H", "A"],         "3. Early Game", "Both HCs in FP", 0),
                Mission(["T", "A"],         "3. Early Game", "All tokens in TTC", 0),
                Mission(["J"],              "3. Early Game", "All 4 jiggies inside Clanker", 0),
                Mission(["R"],              "3. Early Game", "Begin run w/ MM 100% Trotless", 0),
                Mission(["T", "A"],         "3. Early Game", "All tokens in FP", 0),
                Mission(["J"],              "3. Early Game", "Merry Christmas! (Visit Boggy's Igloo w/ him in it & give presents)", 0),
                Mission(["J", "A"],         "3. Early Game", "{} jiggies in FP [r 4-9]".format(random.randint(4,9)), 1),
                Mission(["J", "A"],         "3. Early Game", "9 jiggies in FP", 2),

                Mission(["J", "R"],         "3. Early Game", "No jiggies in MM", 0),
                Mission(["J", "T"],         "3. Early Game", "Termite's Quest: 8 jiggies, 90 notes, & 1 HC as the termite", 0),
                # Mission([],      "3. Early Game", ""),
            ],
            [ # MID_GAME
                Mission(["O", "A"],         "4. Mid Game", "All Jinjos in MMM", 0),
                Mission(["O", "A"],         "4. Mid Game", "All Jinjos in GV", 0),
                Mission(["O", "A"],         "4. Mid Game", "All Jinjos in RBB", 0),
                Mission(["J", "A"],         "4. Mid Game", "{} jiggies in MMM [r 5-10]".format(random.randint(5,10)), 1),
                Mission(["J", "A"],         "4. Mid Game", "All jiggies in MMM", 2),

                Mission(["J", "A"],         "4. Mid Game", "{} jiggies in RBB [r 3-10]".format(random.randint(3,10)), 1),
                Mission(["J", "A"],         "4. Mid Game", "All jiggies in RBB", 2),

                Mission(["N", "A"],         "4. Mid Game", "{} notes in MMM [r 50-100]".format(random.randint(50,100)), 1),
                Mission(["N", "A"],         "4. Mid Game", "All notes in MMM", 2),

                Mission(["N", "A"],         "4. Mid Game", "{} notes in GV [r 40-100]".format(random.randint(40,100)), 1),
                Mission(["N", "A"],         "4. Mid Game", "All notes in GV", 2),

                Mission(["N", "A"],         "4. Mid Game", "{} notes in RBB [r 40-100]".format(random.randint(40,100)), 1),
                Mission(["N", "A"],         "4. Mid Game", "All notes in RBB", 2),

                Mission(["H", "A"],         "4. Mid Game", "Both HCs in MMM", 0),
                Mission(["H", "A"],         "4. Mid Game", "Both HCs in GV", 0),
                Mission(["H", "A"],         "4. Mid Game", "Both HCs in RBB", 0),
                Mission(["T", "A"],         "4. Mid Game", "{} tokens in MMM [r 10-16]".format(random.randint(10,16)), 1),
                Mission(["T", "A"],         "4. Mid Game", "All (16) tokens in MMM", 2),

                Mission(["T", "A"],         "4. Mid Game", "All tokens in GV", 0),
                Mission(["T", "A"],         "4. Mid Game", "{} tokens in RBB [r 10-15]".format(random.randint(10,15)), 1),
                Mission(["T", "A"],         "4. Mid Game", "All tokens in RBB", 2),

                Mission([],                 "4. Mid Game", "MMM witch switch jiggy", 0),
                Mission([],                 "4. Mid Game", "Kill all 10 Limbos (skeletons) in MMM", 0),
                Mission([],                 "4. Mid Game", "GV rings jiggy without flight or bee", 0),
                Mission(["J"],              "4. Mid Game", "Abuse Gobi (beak bust Gobi at all 5 locations)", 0),
                Mission(["J", "A"],         "4. Mid Game", "{} jiggies in GV [r 3-9]".format(random.randint(3,9)), 1),
                Mission(["J", "A"],         "4. Mid Game", "9 Jiggies in GV", 2),

                # Mission([],      "4. Mid Game", ""),
            ],
            [ # LATE_GAME
                Mission(["O", "A"],         "5. Late Game", "All Jinjos in CCW", 0),
                Mission(["O", "A"],         "5. Late Game", "All Jinjos in BGS", 0),
                Mission(["N", "A"],         "5. Late Game", "{} notes in BGS [r 50-100]".format(random.randint(50,100)), 1),
                Mission(["N", "A"],         "5. Late Game", "All notes in BGS", 2),

                Mission(["H", "A"],         "5. Late Game", "Both HCs in BGS", 0),
                Mission(["H", "A"],         "5. Late Game", "Both HCs in CCW", 0),
                Mission(["T", "A"],         "5. Late Game", "All tokens in BGS", 0),
                Mission(["J"],              "5. Late Game", "Croctuses jiggy", 0),
                Mission(["J"],              "5. Late Game", "Tiptup's jiggy", 0),
                Mission(["J"],              "5. Late Game", "Both timed jiggies in BGS", 0),
                Mission([],                 "5. Late Game", "All caterpillars", 0),
                Mission(["J"],              "5. Late Game", "Eyrie's Jiggy", 0),
                Mission(["J"],              "5. Late Game", "Nabnut's Jiggy", 0),
                Mission([],                 "5. Late Game", "Kill all 6 Sir Slushes in winter", 0),
                Mission(["J"],              "5. Late Game", "Flower jiggy in CCW", 0),
                Mission(["N", "A"],         "5. Late Game", "{} notes in CCW [r 30-80]".format(random.randint(30,80)), 1),
                Mission(["N", "A"],         "5. Late Game", "80 notes in CCW", 2),

                Mission(["J", "A"],         "5. Late Game", "{} jiggies in CCW [r 3-8]".format(random.randint(3,8)), 1),
                Mission(["J", "A"],         "5. Late Game", "8 jiggies in CCW", 2),

                Mission(["J"],              "5. Late Game", "{} jiggies in BGS [r 5-8]".format(random.randint(5,8)), 1),
                Mission(["J"],              "5. Late Game", "9 jiggies in BGS", 2),

                Mission(["T", "A"],         "5. Late Game", "{} tokens in CCW [r 15-25]".format(random.randint(15,25)), 1),
                Mission(["T", "A"],         "5. Late Game", "20 tokens in CCW", 2),

                Mission(["J", "T", "R"],    "5. Late Game", "Collect 10 jiggies as the bee", 0),
                # Mission([],      "5. Late Game", ""),
            ]
        ]

# ----------------- LONG MISSION GENERATION -----------------
        if show_missions_var:
            # show missions instead of generating them
            text.config(state = tk.NORMAL)
            text.delete("1.0", tk.END)
            text.insert(tk.END, "LIST OF LONG MISSIONS:\n\n")
            for x in missions:
                text.insert(tk.END, x[0].num+"\n")
                for m in x:
                    if randvar.get() == 1: # if the checkbox is checked (don't randomize goals)
                        if m.rand == 1: continue # if the goal is random don't use it
                    else: # if the checkbox isn't checked (randomize goals)
                        if m.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                    text.insert(tk.END, m.name)
                    if codesvar.get() == 1:
                        text.insert(tk.END, " -- ")
                        text.insert(tk.END, ', '.join(m.codes))
                    text.insert(tk.END, "\n")
                text.insert(tk.END, "\n")
            text.config(state = tk.DISABLED)
            show_missions_var = False

        else:
            goals = []
            codes1 = []
            codes2 = []
            codes3 = []
            i_list = []

            for i in range(len(missions)):
                if i == 0:
                    # do main objective before all else
                    count = len(missions[i])

                    done = False
                    while not done:
                        rn = random.randint(0, count-1)
                        mission = missions[i][rn]
                        if randvar.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        done = True

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
                        if randvar.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
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
                Mission(["H"],              "1. Main Objective", "18 HCs", 0),
                Mission(["T"],              "1. Main Objective", "All 5 tranformations", 0),
                Mission(["O"],              "1. Main Objective", "All Jinjos of any 1 color (your choice)", 0),
                Mission([],                 "1. Main Objective", "All 10 Brentilda visits", 0),
                Mission(["N"],              "1. Main Objective", "Open the 640 note door", 0),
                Mission(["T"],              "2. Side Quest", "{} tokens [r 70-90]".format(random.randint(70,90)), 1),
                Mission(["T"],              "2. Side Quest", "90 tokens", 2),

                Mission(["J"],              "1. Main Objective", "{} jiggies [r 40-55]".format(random.randint(40,55)), 1),
                Mission(["J"],              "1. Main Objective", "45 jiggies", 2),

                Mission([],                 "1. Main Objective", "All 3 Cheato visits", 0),
                Mission([],                 "1. Main Objective", "Activate all 8 warp cauldrons (not Dingpot)", 0),
                Mission(["T"],              "1. Main Objective", "Save Tooty", 0),
                Mission(["J"],              "1. Main Objective", "2 jiggies from each world", 0),
                Mission(["J"],              "1. Main Objective", "All lair jiggies", 0),
            ],
            [ # EARLY_GAME
                Mission(["O", "A"],         "2. Early Game", "All Jinjos in CC", 0),
                Mission(["O", "A"],         "2. Early Game", "All Jinjos in FP", 0),
                Mission(["J", "A"],         "2. Early Game", "{} jiggies in TTC [r 8-10]".format(random.randint(8,10)), 1),
                Mission(["J", "A"],         "2. Early Game", "All jiggies in TTC", 2),

                Mission(["J", "A"],         "2. Early Game", "{} jiggies in CC [r 8-10]".format(random.randint(8,10)), 1),
                Mission(["J", "A"],         "2. Early Game", "All jiggies in CC", 2),

                Mission(["N", "A"],         "2. Early Game", "{} notes in CC [r 75-100]".format(random.randint(75,100)), 1),
                Mission(["N", "A"],         "2. Early Game", "All notes in CC", 2),

                Mission(["N", "A"],         "2. Early Game", "{} notes in FP [r 75-100]".format(random.randint(75,100)), 1),
                Mission(["N", "A"],         "2. Early Game", "All notes in FP", 2),

                Mission(["H", "A"],         "2. Early Game", "Both HCs in TTC", 0),
                Mission(["H", "A"],         "2. Early Game", "Both HCs in CC", 0),
                Mission(["H", "A"],         "2. Early Game", "Both HCs in FP", 0),
                Mission(["T", "A"],         "2. Early Game", "All tokens in TTC", 0),
                Mission(["J"],              "2. Early Game", "All 4 jiggies inside clanker", 0),
                Mission(["R"],              "2. Early Game", "Begin run w/ MM 100% Trotless", 0),
                Mission(["T", "A"],         "2. Early Game", "All tokens in FP", 0),
                Mission(["J"],              "2. Early Game", "Merry Christmas! (Visit Boggy's igloo w/ him in it & give presents)", 0),
                Mission(["J", "A"],         "2. Early Game", "{} jiggies in FP [r 4-9]".format(random.randint(4,9)), 1),
                Mission(["J", "A"],         "2. Early Game", "9 jiggies in FP", 2),

                Mission(["J", "R"],         "2. Early Game", "No jiggies in MM", 0),
                Mission(["J", "T"],         "2. Early Game", "Termite's Quest: 8 jiggies, 90 notes, & 1 HC as the termite", 0),
                Mission(["O", "A"],         "2. Early Game", "All Jinjos in MMM", 0),
                Mission(["J", "A"],         "2. Early Game", "{} jiggies in MMM [r 5-10]".format(random.randint(5,10)), 1),
                Mission(["J", "A"],         "2. Early Game", "All jiggies in MMM", 2),

                Mission(["N", "A"],         "2. Early Game", "{} notes in MMM [r 50-100]".format(random.randint(50,100)), 1),
                Mission(["N", "A"],         "2. Early Game", "All notes in MMM", 2),

                Mission(["H", "A"],         "2. Early Game", "Both HCs in MMM", 0),
                Mission(["T", "A"],         "2. Early Game", "{} tokens in MMM [r 10-16]".format(random.randint(10,16)), 1),
                Mission(["T", "A"],         "2. Early Game", "All (16) tokens in MMM", 2),

                Mission([],                 "2. Early Game", "MMM witch switch jiggy", 0),
                Mission([],                 "2. Early Game", "Kill all 10 Limbos (skeletons) in MMM", 0),
            ],
            [ # LATE_GAME
                Mission(["O", "A"],         "3. Late Game", "All Jinjos in GV", 0),
                Mission(["N", "A"],         "3. Late Game", "{} notes in GV [r 40-100]".format(random.randint(40,100)), 1),
                Mission(["N", "A"],         "3. Late Game", "All notes in GV", 2),

                Mission(["H", "A"],         "3. Late Game", "Both HCs in GV", 0),
                Mission(["T", "A"],         "3. Late Game", "All tokens in GV", 0),
                Mission([],                 "3. Late Game", "GV rings jiggy without flight or bee", 0),
                Mission(["J", "A"],         "3. Late Game", "{} jiggies in GV [r 3-9]".format(random.randint(3,9)), 1),
                Mission(["J", "A"],         "3. Late Game", "9 Jiggies in GV", 2),

                Mission(["J"],              "3. Late Game", "Abuse Gobi (beak bust Gobi at all 5 locations)", 0),
                Mission(["O", "A"],         "3. Late Game", "All Jinjos in RBB", 0),
                Mission(["J", "A"],         "3. Late Game", "{} jiggies in RBB [r 3-10]".format(random.randint(3,10)), 1),
                Mission(["J", "A"],         "3. Late Game", "All jiggies in RBB", 2),

                Mission(["N", "A"],         "3. Late Game", "{} notes in RBB [r 40-100]".format(random.randint(40,100)), 1),
                Mission(["N", "A"],         "3. Late Game", "All notes in RBB", 2),

                Mission(["H", "A"],         "3. Late Game", "Both HCs in RBB", 0),
                Mission(["T", "A"],         "3. Late Game", "{} tokens in RBB [r 10-15]".format(random.randint(10,15)), 1),
                Mission(["T", "A"],         "3. Late Game", "All tokens in RBB", 2),

                Mission(["O", "A"],         "3. Late Game", "All Jinjos in CCW", 0),
                Mission(["O", "A"],         "3. Late Game", "All Jinjos in BGS", 0),
                Mission(["N", "A"],         "3. Late Game", "{} notes in BGS [r 50-100]".format(random.randint(50,100)), 1),
                Mission(["N", "A"],         "3. Late Game", "All notes in BGS", 2),

                Mission(["H", "A"],         "3. Late Game", "Both HCs in BGS", 0),
                Mission(["H", "A"],         "3. Late Game", "Both HCs in CCW", 0),
                Mission(["T", "A"],         "3. Late Game", "All tokens in BGS", 0),
                Mission(["J"],              "3. Late Game", "Croctuses jiggy", 0),
                Mission(["J"],              "3. Late Game", "Tiptup's jiggy", 0),
                Mission(["J"],              "3. Late Game", "Both timed jiggies in BGS", 0),
                Mission([],                 "3. Late Game", "All caterpillars", 0),
                Mission(["J"],              "3. Late Game", "Eyrie's jiggy", 0),
                Mission(["J"],              "3. Late Game", "Nabnut's jiggy", 0),
                Mission([],                 "3. Late Game", "Kill all 6 Sir Slushes in winter", 0),
                Mission(["J"],              "3. Late Game", "Flower jiggy in CCW", 0),
                Mission(["N", "A"],         "3. Late Game", "{} notes in CCW [r 30-80]".format(random.randint(30,80)), 1),
                Mission(["N", "A"],         "3. Late Game", "80 notes in CCW", 2),

                Mission(["J", "A"],         "3. Late Game", "{} jiggies in CCW [r 3-8]".format(random.randint(3,8)), 1),
                Mission(["J", "A"],         "3. Late Game", "8 jiggies in CCW", 2),

                Mission(["J"],              "3. Late Game", "{} jiggies in BGS [r 5-8]".format(random.randint(5,8)), 1),
                Mission(["J"],              "3. Late Game", "9 jiggies in BGS", 2),

                Mission(["T", "A"],         "3. Late Game", "{} tokens in CCW [r 15-25]".format(random.randint(15,25)), 1),
                Mission(["T", "A"],         "3. Late Game", "20 tokens in CCW", 2),
                
                Mission(["J", "T", "R"],    "3. Late Game", "Collect 10 jiggies as the bee", 0),
            ]
        ]

# ----------------- SHORT MISSION GENERATION -----------------
        if show_missions_var:
            # show missions instead of generating them
            text.config(state = tk.NORMAL)
            text.delete("1.0", tk.END)
            text.insert(tk.END, "LIST OF SHORT MISSIONS:\n\n")
            for x in missions:
                text.insert(tk.END, x[0].num+"\n")
                for m in x:
                    if randvar.get() == 1: # if the checkbox is checked (don't randomize goals)
                        if m.rand == 1: continue # if the goal is random don't use it
                    else: # if the checkbox isn't checked (randomize goals)
                        if m.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                    text.insert(tk.END, m.name)
                    if codesvar.get() == 1:
                        text.insert(tk.END, " -- ")
                        text.insert(tk.END, ', '.join(m.codes))
                    text.insert(tk.END, "\n")
                text.insert(tk.END, "\n")
            text.config(state = tk.DISABLED)
            show_missions_var = False
        
        else:
            goals = []
            codes = []
            i_list = []

            for i in range(len(missions)):
                if i == 0:
                    # do main objective before all else
                    count = len(missions[i])

                    done = False
                    while not done:
                        rn = random.randint(0, count-1)
                        mission = missions[i][rn]
                        if randvar.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        done = True
                    
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
                        if randvar.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
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

# -----------------------------------------------------
# ----------------- SHOW ALL MISSIONS -----------------
# -----------------------------------------------------
def print_missions():
    global show_missions_var
    show_missions_var = True
    main()

# --------------------------------------------------
# ----------------- CONFIG BUTTONS -----------------
# --------------------------------------------------
short_check.config(\
    text = "Short (if checked, short\nboard will be generated)", \
    variable = short)

rand_check.config(\
    text = "Unrandomize goals (by default,\ncertain goals are randomized)", \
    variable = randvar)

codes_check.config(\
    text = "Show codes after each goal", \
    variable = codesvar)

main_button.config(\
    text = "Generate Missions", \
    command = main)

missions_button.config(\
    text = "Show List of Missions", \
    command = print_missions)

quit_button.config(\
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

window.title("BK Missions Generator v2.7")
window.minsize(500,300)
window.maxsize(1920,1080)
window.mainloop()