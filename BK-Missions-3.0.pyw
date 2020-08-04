from tkinter import *
from operator import attrgetter
import random


class Mission:
    def __init__(self, codes, num, name, rand):
        self.codes = codes # list of codes, ie ["N", "A"]
        self.num = num # number of goal, ie "1. Main Objective"
        self.name = name # name of goal, ie "Open 765 note door"
        self.rand = rand # 0 means normal, 1 means random, 2 means normal variant of a random goal

show_missions_var = False

# ------------------------------------------------
# ----------------- WINDOW SETUP -----------------
# ------------------------------------------------

win = Tk()

short = IntVar()
codesvar = IntVar()
randvar = IntVar()

top_frame = Frame(win)
top_frame.grid(row = 0, column = 0, columnspan = 3)

def colorchange(b):
    """ b is tk button object, function changes its background color from white->green->red->white """
    if b.cget('bg') == "White":
        b.config(bg = "Green", activebackground = "Green")
    elif b.cget('bg') == "Green":
        b.config(bg = "Red", activebackground = "Red")
    elif b.cget('bg') == "Red":
        b.config(bg = "White", activebackground = "White")

b1t = StringVar(value = "First Goal")
b2t = StringVar(value = "Second Goal")
b3t = StringVar(value = "Third Goal")
b4t = StringVar(value = "Fourth Goal")
b5t = StringVar(value = "Fifth Goal")
btextlist = [b1t, b2t, b3t, b4t, b5t]


b1 = Button(win, textvar = b1t, bg = "White", \
    wraplength = 140, width = 20, command = lambda: colorchange(b1))

b2 = Button(win, textvar = b2t, bg = "White", \
    wraplength = 140, width = 20, command = lambda: colorchange(b2))

b3 = Button(win, textvar = b3t, bg = "White", \
    wraplength = 140, width = 20, command = lambda: colorchange(b3))

b4 = Button(win, textvar = b4t, bg = "White", \
    wraplength = 140, width = 20, command = lambda: colorchange(b4))

b5 = Button(win, textvar = b5t, bg = "White", \
    wraplength = 140, width = 20, command = lambda: colorchange(b5))

blist = [b1, b2, b3, b4, b5]

b1.grid(row = 5, column = 0, sticky='nsew')
b2.grid(row = 6, column = 0, sticky='nsew')
b3.grid(row = 7, column = 0, sticky='nsew')
b4.grid(row = 8, column = 0, sticky='nsew')
b5.grid(row = 9, column = 0, sticky='nsew')

t1 = Text(win, height = 7, width = 15)
t2 = Text(win, height = 7, width = 15)
t3 = Text(win, height = 7, width = 15)
t4 = Text(win, height = 7, width = 15)
t5 = Text(win, height = 7, width = 15)

tlist = [t1, t2, t3, t4, t5]

t1.grid(row = 5, column = 1, sticky='nsew')
t2.grid(row = 6, column = 1, sticky='nsew')
t3.grid(row = 7, column = 1, sticky='nsew')
t4.grid(row = 8, column = 1, sticky='nsew')
t5.grid(row = 9, column = 1, sticky='nsew')

s1 = Scrollbar(win)
s2 = Scrollbar(win)
s3 = Scrollbar(win)
s4 = Scrollbar(win)
s5 = Scrollbar(win)

slist = [s1, s2, s3, s4, s5]

s1.grid(row = 5, column = 2, sticky='nsew')
s2.grid(row = 6, column = 2, sticky='nsew')
s3.grid(row = 7, column = 2, sticky='nsew')
s4.grid(row = 8, column = 2, sticky='nsew')
s5.grid(row = 9, column = 2, sticky='nsew')

t1['yscrollcommand'] = s1.set
t2['yscrollcommand'] = s2.set
t3['yscrollcommand'] = s3.set
t4['yscrollcommand'] = s4.set
t5['yscrollcommand'] = s5.set


# ========================================================================================================
# ========================================================================================================
# ========================================================================================================
def main():
    """ main function, gets a set of missions randomly
        based on certain restricitons """
    global short
    global show_missions_var
    global codesvar

    for t in tlist:
        # clear text boxes
        t.delete("1.0", END)
    for m in blist:
        # set backgrounds back to white
        m.config(bg = "White")
    # define missions
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
                Mission(["J"],              "1. Main Objective", "Humanitarian: Jiggies: Chimpy, Blubber, raise Clanker/fix both teeth, Tanktup, presents in FP, Gobi's rock, Trunker, Snorkel, Nabut, Eyrie.\nOthers (no jiggy): Gnawty's Boulder, Tooty", 0),
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
            new_win = Toplevel()
            new_win.title = "Missions List"
            text = Text(new_win)
            text.grid(row = 0, column = 0)

            text.config(state = NORMAL)
            text.delete("1.0", END)
            text.insert(END, "LIST OF LONG MISSIONS:\n\n")
            for x in missions:
                text.insert(END, x[0].num+"\n")
                for m in x:
                    if randvar.get() == 1: # if the checkbox is checked (don't randomize goals)
                        if m.rand == 1: continue # if the goal is random don't use it
                    else: # if the checkbox isn't checked (randomize goals)
                        if m.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                    text.insert(END, '-' + m.name)
                    if codesvar.get() == 1:
                        text.insert(END, " -- ")
                        text.insert(END, ', '.join(m.codes))
                    text.insert(END, "\n")
                text.insert(END, "\n")
            text.config(state = DISABLED)
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
                # write the goals to the buttons
                for i,g in enumerate(goals_sort):
                    if codesvar.get() == 1:
                        btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
                    else: 
                        btextlist[i].set(g.name)
    
    elif short.get() == 1:
# ----------------- SHORT MISSION LIST -----------------
        missions = [
            [ # MAIN_OBJECTIVE
                Mission(["H"],              "1. Main Objective", "18 HCs", 0),
                Mission(["T"],              "1. Main Objective", "All 5 tranformations", 0),
                Mission(["O"],              "1. Main Objective", "All Jinjos of any 1 color (your choice)", 0),
                Mission([],                 "1. Main Objective", "All 10 Brentilda visits", 0),
                Mission(["N"],              "1. Main Objective", "Open the 640 note door", 0),
                Mission(["T"],              "1. Main Objective", "{} tokens [r 70-90]".format(random.randint(70,90)), 1),
                Mission(["T"],              "1. Main Objective", "90 tokens", 2),

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
            new_win = Toplevel()
            new_win.title = "Missions List"
            text = Text(new_win)
            text.grid(row = 0, column = 0)

            text.config(state = NORMAL)
            text.delete("1.0", END)
            text.insert(END, "LIST OF SHORT MISSIONS:\n\n")
            for x in missions:
                text.insert(END, x[0].num+"\n")
                for m in x:
                    if randvar.get() == 1: # if the checkbox is checked (don't randomize goals)
                        if m.rand == 1: continue # if the goal is random don't use it
                    else: # if the checkbox isn't checked (randomize goals)
                        if m.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                    text.insert(END, '-' + m.name)
                    if codesvar.get() == 1:
                        text.insert(END, " -- ")
                        text.insert(END, ', '.join(m.codes))
                    text.insert(END, "\n")
                text.insert(END, "\n")
            text.config(state = DISABLED)
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

                    # comment this code below to enable repeating codes for early/late game
                    # if it's commented out that means codes can repeat for 2/3 (as long as they don't share 1's goal)
                    # vvvvvvvvvvvvvvvvvvvvvvv
                    for c in mission.codes:
                        codes.append(c)
                    # ^^^^^^^^^^^^^^^^^^^^^^^
                
                    goals.append(mission)
                goals_sort = sorted(goals, key=attrgetter('num'))
                # write the goals to the buttons
                for i,g in enumerate(goals_sort):
                    if codesvar.get() == 1:
                        btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
                    else: 
                        btextlist[i].set(g.num + g.name)
                b4t.set("-----")
                b5t.set("-----")

# --------------------------------------------------
# ----------------- MORE FUNCTIONS -----------------
# --------------------------------------------------
def mission_list():
    global show_missions_var
    show_missions_var = True
    main()

def rem_text():
    for t in tlist:
        t.grid_forget()
    for s in slist:
        s.grid_forget()
    # win.geometry("150x675")
    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=0)

def shw_text():
    win.grid_columnconfigure(0, weight=0)
    win.grid_columnconfigure(1, weight=1)
    for i,t in enumerate(tlist):
        t.grid(row = i+5, column = 1, sticky='nsew')
    for i,s in enumerate(slist):
        s.grid(row = i+5, column = 2, sticky='nsew')
    # win.geometry("360x675")

def clr_text():
    for t in tlist:
        t.delete("1.0", END)


def show_settings():
    settings_win = Toplevel(win)
    settings_win.title("Settings")
    new_quit_button = Button(settings_win, text = "Exit Settings", command = settings_win.destroy)

    short_check = Checkbutton(settings_win, text = "Short (if checked, short\nboard will be generated)", variable = short)

    rand_check = Checkbutton(settings_win, text = "Unrandomize goals (by default,\ncertain goals are randomized)", variable = randvar)

    codes_check = Checkbutton(settings_win, text = "Show codes after each goal", variable = codesvar)

    remove_text = Button(settings_win, text = "Hide Text Boxes", command = rem_text)

    show_text = Button(settings_win, text = "Show Text Boxes", command = shw_text)

    clear_text = Button(settings_win, text = "Clear Text Boxes", command = clr_text)

    short_check.grid(row = 0, column = 0, pady=10, columnspan = 2)
    codes_check.grid(row = 1, column = 0, pady=10, columnspan = 2)
    rand_check.grid(row = 2, column = 0, pady=10, columnspan = 2)
    remove_text.grid(row = 3, column = 0, pady=10)
    show_text.grid(row = 3, column = 1, pady=10)
    clear_text.grid(row = 4, column = 0, columnspan = 2)
    new_quit_button.grid(row = 5, column = 0, columnspan = 2, pady=10)
    settings_win.geometry("200x290")
    settings_win.minsize(200, 290)


# -------------------------------------------------
# ----------------- BUTTON CONFIG -----------------
# -------------------------------------------------

gen_missions = Button(top_frame, text = "Generate Missions", command = main)
# gen_missions.pack()
gen_missions.grid(row = 0, column = 3, pady = 6)

show_missions = Button(top_frame, text = "Show list of missions", command = mission_list)
# show_missions.pack()
show_missions.grid(row = 1, column = 3, pady = 6)


settings = Button(top_frame, text = "Settings", command = show_settings)
# settings.pack()
settings.grid(row = 2, column = 3, pady = 6)


# win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
for i in range(5, 10):
    win.grid_rowconfigure(i, weight = 1)


win.title("BK Missions Generator v3.0")
win.geometry("360x675")
win.minsize(150, 675)
# win.maxsize(1920,1080)
win.mainloop()