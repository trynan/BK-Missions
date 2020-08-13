# Original version by Trynan and Wedarobi
# Maintained by Trynan
# 8/11/2020

from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
from operator import attrgetter
import random
import configparser

config = configparser.ConfigParser()
config.read('bk_config.ini')
default_vals_list = []
for key in config['settings']:
    default_vals_list.append(config['settings'][key])

class Mission:
    def __init__(self, codes, num, name, rand):
        self.codes = codes # list of codes, ie ["N", "A"]
        self.num = num # number of goal, ie "1. Main Objective"
        self.name = name # name of goal, ie "Open 765 note door"
        self.rand = rand # 0 means normal, 1 means random, 2 means normal variant of a random goal

show_missions_var = False

def colorchange(b):
    """ b is tk button object, function changes its background color from white->green->red->white """
    if b.cget('bg') == "White":
        b.config(bg = "Green", activebackground = "Green")
    elif b.cget('bg') == "Green":
        b.config(bg = "Red", activebackground = "Red")
    elif b.cget('bg') == "Red":
        b.config(bg = "White", activebackground = "White")

# ------------------------------------------------
# ----------------- WINDOW SETUP -----------------
# ------------------------------------------------

# -------------------- VARIABLE SETUP --------------------
win = Tk()

short_var = IntVar() # 0 or 1
codes_var = IntVar() # 0 or 1
rand_var = IntVar() # 0 or 1
win_size_var = StringVar() # format: 360x675+100+100 --> width x height + xoffset + yoffset
show_text_var = IntVar() # 0 or 1
font_size_var = IntVar() # positive integer
varlist = [short_var, codes_var, rand_var, win_size_var, show_text_var, font_size_var]

# set all of these configuarables to their defaults as dictated by the config file
for i,val in enumerate(default_vals_list):
    varlist[i].set(val)

default_font = tkFont.Font(family = 'TkTextFont', size = font_size_var.get())

# -------------------- WIDGET INITIALIZATION --------------------
top_frame = Frame(win)
top_frame.grid(row = 0, column = 0, columnspan = 3)

b1t = StringVar(value = "First Goal")
b2t = StringVar(value = "Second Goal")
b3t = StringVar(value = "Third Goal")
b4t = StringVar(value = "Fourth Goal")
b5t = StringVar(value = "Fifth Goal")
btextlist = [b1t, b2t, b3t, b4t, b5t]

b1 = Button(win, command = lambda: colorchange(b1))
b2 = Button(win, command = lambda: colorchange(b2))
b3 = Button(win, command = lambda: colorchange(b3))
b4 = Button(win, command = lambda: colorchange(b4))
b5 = Button(win, command = lambda: colorchange(b5))
blist = [b1, b2, b3, b4, b5]

t1 = Text(win)
t2 = Text(win)
t3 = Text(win)
t4 = Text(win)
t5 = Text(win)
tlist = [t1, t2, t3, t4, t5]

s1 = Scrollbar(win)
s2 = Scrollbar(win)
s3 = Scrollbar(win)
s4 = Scrollbar(win)
s5 = Scrollbar(win)
slist = [s1, s2, s3, s4, s5]

# -------------------- WIDGET CONFIG --------------------
for i,b in enumerate(blist):
    b.grid(row = i+5, column = 0, sticky = 'nsew')
    b.config(textvar = btextlist[i], bg = "White", width = 20, font = default_font)
    if show_text_var.get() == 0:
        size = config['settings']['win_size'][0:4]
        if 'x' in size: # number is 3 digits and not 4
            size = size[0:3]
        b.config(wraplength = size)
    else:
        b.config(wraplength = 165)
if short_var.get() == 1:
    b4t.set("-----")
    b5t.set("-----")
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)

for i,t in enumerate(tlist):
    t.config(height = 7, width = 15, font = default_font)
    t.grid(row = i+5, column = 1, sticky='nsew')
    t['yscrollcommand'] = slist[i].set

for i,s in enumerate(slist):
    s.config(command = tlist[i].yview)
    s.grid(row = i+5, column = 2, sticky='nsew')

# ----------------------------------------------------
# ----------------- BUTTON FUNCTIONS -----------------
# ----------------------------------------------------
def get_current_size(t):
    """ t is the text field to put the result into """
    t.delete(0, END)
    t.insert(END, win.winfo_geometry())

def remove_text_f(b, c):
    """ b is the button you pressed to call this function, so it will be greyed out.
        c is the other button that will now be un-greyed out. """
    show_text_var.set(0)
    for t in tlist:
        t.grid_forget()
    for s in slist:
        s.grid_forget()
    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=0)
    for button in blist:
        button.config(wraplength = win.winfo_width())
    c.config(state = NORMAL)
    b.config(state = DISABLED)

def show_text_f(b, c):
    """ b is the button you pressed to call this function, so it will be greyed out.
        c is the other button that will now be un-greyed out. """
    show_text_var.set(1)
    win.grid_columnconfigure(0, weight=0)
    win.grid_columnconfigure(1, weight=1)
    for i,t in enumerate(tlist):
        t.grid(row = i+5, column = 1, sticky='nsew')
    for i,s in enumerate(slist):
        s.grid(row = i+5, column = 2, sticky='nsew')
    for button in blist:
        button.config(wraplength = 165)
    c.config(state = NORMAL)
    b.config(state = DISABLED)

def clear_text_f():
    for t in tlist:
        t.delete("1.0", END)

def apply_settings_f(t1, t2):
    """ t1 is an entry window that we need text from. so is t2 """
    global win_size_var
    global font_size_var
    new_win_size = t1.get()
    new_font_size = t2.get()
    win_size_var.set(new_win_size)
    font_size_var.set(new_font_size)
    default_font.config(size = new_font_size)
    win.geometry(new_win_size)
    for b in blist:
        if show_text_var.get() == 0:
            b.config(wraplength = win.winfo_width())
        else:
            b.config(wraplength = 165)

def set_default_f():
    for i,key in enumerate(config['settings']):
        config.set('settings', key, str(varlist[i].get())) # since it's .get() you don't have to directly update varlist
    with open('bk_config.ini', 'w') as configfile:
        config.write(configfile)

# ========================================================================================================
# ========================================================================================================
# ========================================================================================================
def main():
    """ main function, gets a set of missions randomly
        based on certain restricitons """
    global short_var
    global show_missions_var
    global codes_var

    for t in tlist:
        # clear text boxes
        t.delete("1.0", END)
    for m in blist:
        # set backgrounds back to white
        m.config(bg = "White")
    # define missions
    if short_var.get() == 0:
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

# ----------------- SHOW LONG MISSIONS -----------------
        if show_missions_var:
            # show missions instead of generating them
            new_win = Toplevel()
            new_win.grab_set()
            new_win.title = "Missions List"
            text = Text(new_win, font = default_font)
            scroll = Scrollbar(new_win, command = text.yview)
            text['yscrollcommand'] = scroll.set
            text.grid(row = 0, column = 0, sticky = 'nsew')
            scroll.grid(row = 0, column = 1, sticky = 'nsew')
            new_win.grid_columnconfigure(0, weight = 1)
            new_win.grid_rowconfigure(0, weight = 1)

            text.config(state = NORMAL)
            text.delete("1.0", END)
            text.insert(END, "LIST OF LONG MISSIONS:\n\n")
            for x in missions:
                text.insert(END, x[0].num+"\n")
                for m in x:
                    if rand_var.get() == 1: # if the checkbox is checked (don't randomize goals)
                        if m.rand == 1: continue # if the goal is random don't use it
                    else: # if the checkbox isn't checked (randomize goals)
                        if m.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                    text.insert(END, '-' + m.name)
                    if codes_var.get() == 1:
                        text.insert(END, " -- ")
                        text.insert(END, ', '.join(m.codes))
                    text.insert(END, "\n")
                text.insert(END, "\n")
            text.config(state = DISABLED)
            show_missions_var = False

# ----------------- LONG MISSION GENERATION -----------------
        else:
            b4.config(state = NORMAL)
            b5.config(state = NORMAL)
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
                        if rand_var.get() == 1: # nonrandoms only
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
                        if rand_var.get() == 1: # nonrandoms only
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
                    if codes_var.get() == 1:
                        btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
                    else: 
                        btextlist[i].set(g.name)
    
    elif short_var.get() == 1:

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

# ----------------- SHOW SHORT MISSIONS -----------------
        if show_missions_var:
            # show missions instead of generating them
            new_win = Toplevel()
            new_win.grab_set()
            new_win.title = "Missions List"
            text = Text(new_win, font = default_font)
            scroll = Scrollbar(new_win, command = text.yview)
            text['yscrollcommand'] = scroll.set
            text.grid(row = 0, column = 0, sticky = 'nsew')
            scroll.grid(row = 0, column = 1, sticky = 'nsew')
            new_win.grid_columnconfigure(0, weight = 1)
            new_win.grid_rowconfigure(0, weight = 1)


            text.config(state = NORMAL)
            text.delete("1.0", END)
            text.insert(END, "LIST OF SHORT MISSIONS:\n\n")
            for x in missions:
                text.insert(END, x[0].num+"\n")
                for m in x:
                    if rand_var.get() == 1: # if the checkbox is checked (don't randomize goals)
                        if m.rand == 1: continue # if the goal is random don't use it
                    else: # if the checkbox isn't checked (randomize goals)
                        if m.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                    text.insert(END, '-' + m.name)
                    if codes_var.get() == 1:
                        text.insert(END, " -- ")
                        text.insert(END, ', '.join(m.codes))
                    text.insert(END, "\n")
                text.insert(END, "\n")
            text.config(state = DISABLED)
            show_missions_var = False

# ----------------- LONG MISSION GENERATION -----------------        
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
                        if rand_var.get() == 1: # nonrandoms only
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
                        if rand_var.get() == 1: # nonrandoms only
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
                    if codes_var.get() == 1:
                        btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
                    else: 
                        btextlist[i].set(g.name)
                b4t.set("-----")
                b5t.set("-----")
                b4.config(state = DISABLED)
                b5.config(state = DISABLED)
# ========================================================================================================
# ========================================================================================================
# ========================================================================================================

# --------------------------------------------------
# ----------------- MORE FUNCTIONS -----------------
# --------------------------------------------------
def mission_list():
    global show_missions_var
    show_missions_var = True
    main()

def show_settings():
    settings_win = Toplevel(win)
    settings_win.title("Settings")
    settings_win.grab_set()
    top_labelframe = LabelFrame(settings_win, text = "Missions Generation")
    mid_labelframe = LabelFrame(settings_win, text = "Display/Window Settings")
    bottom_labelframe = LabelFrame(settings_win, text = "Apply and Exit")

    top_labelframe.pack(padx = 10, pady = 10, expand = TRUE, fill = BOTH)
    mid_labelframe.pack(padx = 10, pady = 10, expand = TRUE, fill = BOTH)
    bottom_labelframe.pack(padx = 10, pady = 10, expand = TRUE, fill = BOTH)

    font_frame = Frame(mid_labelframe)
    window_frame = Frame(mid_labelframe)
    size_frame = Frame(mid_labelframe)
    textbox_frame = Frame(mid_labelframe)
    cleartext_frame = Frame(mid_labelframe)

    font_frame.pack(padx = 10, pady = 5)
    window_frame.pack(padx = 10, pady = 5)
    size_frame.pack(padx = 10, pady = 5)
    textbox_frame.pack(padx = 10, pady = 5)
    cleartext_frame.pack(padx = 10, pady = 5)
    
    short_check = Checkbutton(top_labelframe, text = "Short (if checked, short\nboard will be generated)", font = default_font, variable = short_var)
    codes_check = Checkbutton(top_labelframe, text = "Show codes after each goal", font = default_font, variable = codes_var)
    rand_check = Checkbutton(top_labelframe, text = "Unrandomize goals (by default,\ncertain goals are randomized)", font = default_font, variable = rand_var)
    font_size_label = Label(font_frame, text = "Font size\n(default: 10)", font = default_font)
    font_size = Entry(font_frame, textvariable = font_size_var, width = 8)
    win_size_label = Label(window_frame, text = "Window size\n(default: 360x775)", font = default_font)
    win_size = Entry(window_frame, textvariable = win_size_var, width = 18)
    current_size = Button(size_frame, text = "Get current size/position", font = default_font, command = lambda: get_current_size(win_size))
    remove_text = Button(textbox_frame, text = "Hide text boxes", font = default_font, command = lambda: remove_text_f(remove_text, show_text))
    show_text = Button(textbox_frame, text = "Show text boxes", font = default_font, command = lambda: show_text_f(show_text, remove_text))
    clear_text = Button(cleartext_frame, text = "Clear text boxes", font = default_font, command = clear_text_f)
    apply_settings = Button(bottom_labelframe, text = "Apply settings", font = default_font, command = lambda: apply_settings_f(win_size, font_size))
    set_default = Button(bottom_labelframe, text = "Set current values as defaults", font = default_font, command = set_default_f)
    new_quit = Button(bottom_labelframe, text = "Exit settings", font = default_font, command = settings_win.destroy)

    short_check.pack(padx = 10, pady = 5)
    codes_check.pack(padx = 10, pady = 5)
    rand_check.pack(padx = 10, pady = 5)

    font_size_label.grid(row = 0, column = 0)
    font_size.grid(row = 0, column = 1, padx = 10)
    win_size_label.grid(row = 1, column = 0)
    win_size.grid(row = 1, column = 1, padx = 10)
    current_size.grid(row = 2, column = 1, padx = 10)
    remove_text.grid(row = 3, column = 0, padx = 10)
    show_text.grid(row = 3, column = 1, padx = 10)
    clear_text.grid(row = 4, column = 0, columnspan = 2, padx = 10)

    apply_settings.pack(padx = 10, pady = 5)
    set_default.pack(padx = 10, pady = 5)
    new_quit.pack(padx = 10, pady = 5)

    if show_text_var.get() == 0:
        remove_text.config(state = DISABLED)
    else:
        show_text.config(state = DISABLED)

# ---------------------------------------------------
# ----------------- FINAL UI CONFIG -----------------
# ---------------------------------------------------

# -------------------- MAIN THREE BUTTONS --------------------
gen_missions = Button(top_frame, text = "Generate Missions", font = default_font, command = main)
show_missions = Button(top_frame, text = "Show list of missions", font = default_font, command = mission_list)
settings = Button(top_frame, text = "Settings", font = default_font, command = show_settings)

gen_missions.grid(row = 0, column = 3, pady = 6)
show_missions.grid(row = 1, column = 3, pady = 6)
settings.grid(row = 2, column = 3, pady = 6)

# -------------------- WINDOW CONFIG AND LAST STEPS --------------------
win.grid_columnconfigure(1, weight = 1)
for i in range(5, 10):
    win.grid_rowconfigure(i, weight = 1)

if config['settings']['show_text'] == '0':
    for t in tlist:
        t.grid_forget()
    for s in slist:
        s.grid_forget()
    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=0)

win.title("BK Missions Generator v3.1")
win.geometry(win_size_var.get())
win.minsize(170, 675)
win.mainloop()