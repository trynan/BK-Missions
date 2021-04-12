# Original version by Trynan and Wedarobi
# Maintained by Trynan
# 8/11/2020
# current: 2/24/2021

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
    def __init__(self, rand, codes, name):
        self.rand = rand # 0 means normal, 1 means random, 2 means normal variant of a random goal
        self.codes = codes # list of codes, ie ["N", "A"]
        self.name = name # name of goal, ie "Open 765 note door"
    
    def def_num(self, num):
        self.num = num


# ------------------------------------------------
# ----------------- WINDOW SETUP -----------------
# ------------------------------------------------

# -------------------- VARIABLE SETUP --------------------
win = Tk()

show_missions_var   = False
short_var           = IntVar() # 0 or 1
codes_var           = IntVar() # 0 or 1
rand_var            = IntVar() # 0 or 1
win_size_var        = StringVar() # format: 360x675+100+100 --> width x height + xoffset + yoffset
show_text_var       = IntVar() # 0 or 1
font_size_var       = IntVar() # positive integer
seed_value          = StringVar() # six digit number
custom_seed_value   = StringVar() # can be any string, i think
seed_var            = IntVar() # 0 or 1
varlist             = [short_var, codes_var, rand_var, win_size_var, show_text_var, font_size_var]
long_label_list = [
    "1. Main Objective",
    "2. Side Quest",
    "3. Early Game",
    "4. Mid Game",
    "5. Late Game"
]
short_label_list = [
    "1. Main Objective",
    "2. Early Game",
    "3. Late Game"
]
jinjo_list = [
    "purple",
    "green",
    "blue",
    "yellow",
    "orange"
]
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
def colorchange(b):
    """ b is tk button object, function changes its background color from white->green->red->white """
    if b.cget('bg') == "White":
        b.config(bg = "Green", activebackground = "Green")
    elif b.cget('bg') == "Green":
        b.config(bg = "Red", activebackground = "Red")
    elif b.cget('bg') == "Red":
        b.config(bg = "White", activebackground = "White")

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
    # if custom_seed_value.get() != '':
    if seed_var.get() == 1:
        random.seed(custom_seed_value.get())
        seed_value.set(custom_seed_value.get())
    else:
        random.seed() # randomize current seed based on system time
        rn = random.randrange(999999)
        seed_value.set(rn)
        custom_seed_value.set(rn)
        random.seed(seed_value.get())

    for t in tlist:
        # clear text boxes
        t.delete("1.0", END)
    for m in blist:
        # set backgrounds back to white
        m.config(bg = "White")
    # define missions
    long_main = [
        Mission(0, ["N"],           "Open 765 note door"),
        Mission(0, ["O"],           "All Jinjos"),
        Mission(0, ["N"],           "Defeat Grunty"),
        Mission(0, ["H", "T"],      "All 24 honeycombs"),
        Mission(0, ["T"],           "All 116 tokens"),
        Mission(0, ["J"],           "Open all 9 worlds"),
        Mission(0, ["N", "R"],      "All notes"),
        Mission(1, ["J", "R"],      "{} jiggies [r 75-90]".format(random.randint(75,90))),
        Mission(2, ["J", "R"],      "85 jiggies"),
        Mission(0, ["N", "J", "R"], "Open DoG & defeat Grunty"),
        Mission(0, ["J"],           "Humanitarian: Jiggies: Chimpy, Blubber, raise Clanker/fix both teeth, Tanktup, presents in FP, Gobi's rock, Trunker, Snorkel, Nabut, Eyrie.\nOthers (no jiggy): Gnawty's Boulder, Tooty"),
        Mission(0, ["N", "R"],      "Open All 12 Note Doors and Defeat Grunty"),
        Mission(0, ["A"],           "All of 1 type of collectible from each world (all tokens, honeycombs, notes, or jiggies, must do at least one of each in a unique world)"),
    ]
    long_side = [
        Mission(1, ["H", "A"],      "{} HCs [r 14-18]".format(random.randint(14,18))),
        Mission(2, ["H", "A"],      "18 HCs"),
        Mission(0, ["T"],           "All 5 transformations"),
        Mission(0, [],              "All 10 Brentilda visits"),
        Mission(0, ["O"],           "All 9 {} Jinjos (color randomly chosen)".format(jinjo_list[random.randint(0,4)])),
        Mission(0, ["N"],           "Open the 640 note door"),
        Mission(1, ["T"],           "{} tokens [r 70-90]".format(random.randint(70,90))),
        Mission(2, ["T"],           "90 tokens"),
        Mission(1, ["J"],           "{} jiggies [r 40-60]".format(random.randint(40,60))),
        Mission(2, ["J"],           "45 jiggies"),
        Mission(0, [],              "All 3 Cheato Visits"),
        Mission(0, ["J"],           "2 jiggies from each world"),
        Mission(0, ["J"],           "All lair jiggies"),
        Mission(0, [],              "Activate all 8 warp cauldrons (not Dingpot)"),
        Mission(0, ["R"],           "No RBA"),
        Mission(0, ["R"],           "No FFM"),
        Mission(0, ["R", "J"],      "No MMM early"),
        Mission(0, ["R", "J"],      "No FP early"),
    ]
    short_main = [
        Mission(1, ["H"],           "{} HCs [r 14-18] ".format(random.randint(14,18))),
        Mission(2, ["H"],           "18 HCs"),
        Mission(0, ["T"],           "All 5 tranformations"),
        Mission(0, ["O"],           "All Jinjos of any 1 color (your choice)"),
        Mission(0, [],              "All 10 Brentilda visits"),
        Mission(0, ["N"],           "Open the 640 note door"),
        Mission(1, ["T"],           "{} tokens [r 70-90]".format(random.randint(70,90))),
        Mission(2, ["T"],           "90 tokens"),
        Mission(1, ["J"],           "{} jiggies [r 45-60]".format(random.randint(45,60))),
        Mission(2, ["J"],           "45 jiggies"),
        Mission(0, [],              "All 3 Cheato visits"),
        Mission(0, [],              "Activate all 8 warp cauldrons (not Dingpot)"),
        Mission(0, ["T"],           "Save Tooty"),
        Mission(0, ["J"],           "2 jiggies from each world"),
        Mission(0, ["J"],           "All lair jiggies"),
    ]
    mm = [
        Mission(0, ["R"],           "Begin run w/ MM 100% Trotless"),
        Mission(0, ["J", "R"],      "No more than 2 jiggies in MM"),
        Mission(0, [],              "Termite's Quest: 5 jiggies and 1 HC as the termite"),
    ]
    ttc = [
        Mission(1, ["J", "A"],      "{} jiggies in TTC [r 8-10]".format(random.randint(8,10))),
        Mission(2, ["J", "A"],      "All jiggies in TTC"),
        Mission(0, ["H", "A"],      "Both HCs in TTC"),
        Mission(0, ["T", "A"],      "All tokens in TTC"),
    ]
    cc = [
        Mission(0, ["O", "A"],      "All Jinjos in CC"),
        Mission(1, ["J", "A"],      "{} jiggies in CC [r 8-10]".format(random.randint(8,10))),
        Mission(2, ["J", "A"],      "All jiggies in CC"),
        Mission(1, ["N", "A"],      "{} notes in CC [r 80-100]".format(random.randint(80,100))),
        Mission(2, ["N", "A"],      "All notes in CC"),
        Mission(0, ["H", "A"],      "Both HCs in CC"),
        Mission(0, ["J"],           "All 4 jiggies inside Clanker"),
    ]
    fp = [
        Mission(0, ["O", "A"],      "All Jinjos in FP"),
        Mission(1, ["N", "A"],      "{} notes in FP [r 80-100]".format(random.randint(80,100))),
        Mission(2, ["N", "A"],      "All notes in FP"),
        Mission(0, ["H", "A"],      "Both HCs in FP"),
        Mission(0, ["T", "A"],      "All tokens in FP"),
        Mission(0, ["J"],           "Merry Christmas! (Visit Boggy's igloo w/ him in it & give presents)"),
        Mission(1, ["J", "A"],      "{} jiggies in FP [r 4-9]".format(random.randint(4,9))),
        Mission(2, ["J", "A"],      "9 jiggies in FP"),	
    ]
    mmm = [
        Mission(0, ["O", "A"],      "All Jinjos in MMM"),
        Mission(1, ["J", "A"],      "{} jiggies in MMM [r 6-10]".format(random.randint(6,10))),
        Mission(2, ["J", "A"],      "All jiggies in MMM"),
        Mission(1, ["N", "A"],      "{} notes in MMM [r 60-100]".format(random.randint(60,100))),
        Mission(2, ["N", "A"],      "All notes in MMM"),
        Mission(0, ["H", "A"],      "Both HCs in MMM"),
        Mission(1, ["T", "A"],      "{} tokens in MMM [r 10-16]".format(random.randint(10,16))),
        Mission(2, ["T", "A"],      "All (16) tokens in MMM"),
        Mission(0, [],              "MMM witch switch jiggy"),
        Mission(0, [],              "Kill all 10 Limbos (skeletons) in MMM"),
    ]
    gv = [
        Mission(0, ["O", "A"],      "All Jinjos in GV"),
        Mission(1, ["N", "A"],      "{} notes in GV [r 40-100]".format(random.randint(40,100))),
        Mission(2, ["N", "A"],      "All notes in GV"),
        Mission(0, ["H", "A"],      "Both HCs in GV"),
        Mission(0, ["T", "A"],      "All tokens in GV"),
        Mission(0, [],              "GV rings jiggy without flight or bee"),
        Mission(1, ["J", "A"],      "{} jiggies in GV [r 4-9]".format(random.randint(4,9))),
        Mission(2, ["J", "A"],      "9 Jiggies in GV"),
        Mission(0, ["J"],           "Abuse Gobi (beak bust Gobi at all 5 locations)"),
    ]
    rbb = [
        Mission(0, ["O", "A"],      "All Jinjos in RBB"),
        Mission(1, ["J", "A"],      "{} jiggies in RBB [r 4-10]".format(random.randint(4,10))),
        Mission(2, ["J", "A"],      "All jiggies in RBB"),
        Mission(1, ["N", "A"],      "{} notes in RBB [r 40-100]".format(random.randint(40,100))),
        Mission(2, ["N", "A"],      "All notes in RBB"),
        Mission(0, ["H", "A"],      "Both HCs in RBB"),
        Mission(1, ["T", "A"],      "{} tokens in RBB [r 10-15]".format(random.randint(10,15))),
        Mission(2, ["T", "A"],      "All tokens in RBB"),
    ]
    bgs = [
        Mission(0, ["O", "A"],      "All Jinjos in BGS"),
        Mission(1, ["N", "A"],      "{} notes in BGS [r 75-100]".format(random.randint(75,100))),
        Mission(2, ["N", "A"],      "All notes in BGS"),
        Mission(0, ["H", "A"],      "Both HCs in BGS"),
        Mission(0, ["T", "A"],      "All tokens in BGS"),
        Mission(0, ["J"],           "Croctuses jiggy"),
        Mission(0, ["J"],           "Tiptup's jiggy"),
        Mission(0, ["J"],           "Both timed jiggies in BGS"),
        Mission(1, ["J"],           "{} jiggies in BGS [r 5-8]".format(random.randint(5,8))),
        Mission(2, ["J"],           "9 jiggies in BGS"),
    ]
    ccw = [
        Mission(0, ["O", "A"],      "All Jinjos in CCW"),
        Mission(0, ["H", "A"],      "Both HCs in CCW"),
        Mission(0, [],              "All 21 caterpillars"),
        Mission(0, [],              "Eyrie's jiggy"),
        Mission(0, ["J"],           "Nabnut's jiggy"),
        Mission(0, [],              "Kill all 6 Sir Slushes in winter"),
        Mission(0, ["J"],           "Flower jiggy in CCW"),
        Mission(1, ["N", "A"],      "{} notes in CCW [r 50-80]".format(random.randint(50,80))),
        Mission(2, ["N", "A"],      "80 notes in CCW"),
        Mission(1, ["J", "A"],      "{} jiggies in CCW [r 4-8]".format(random.randint(4,8))),
        Mission(2, ["J", "A"],      "8 jiggies in CCW"),
        Mission(1, ["T", "A"],      "{} tokens in CCW [r 15-25]".format(random.randint(15,25))),
        Mission(2, ["T", "A"],      "20 tokens in CCW"),
        Mission(0, ["J", "T", "R"], "Collect 8 jiggies as the bee"),
    ]

    if short_var.get() == 0:
# ----------------- LONG MISSION LIST -----------------
        missions = [
            [ # MAIN_OBJECTIVE
                long_main
            ],
            [ # SIDE_QUEST
                long_side
            ],
            [ # EARLY_GAME
                mm,
                ttc,
                cc,
                fp,
            ],
            [ # MID_GAME
                mmm,
                gv,
                rbb
            ],
            [ # LATE_GAME
                bgs,
                ccw
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
            for a,x in enumerate(missions):
                text.insert(END, long_label_list[a]+"\n")
                for c in x:
                    for g in c:
                        if rand_var.get() == 1: # if the checkbox is checked (don't randomize goals)
                            if g.rand == 1: continue # if the goal is random don't use it
                        else: # if the checkbox isn't checked (randomize goals)
                            if g.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                        text.insert(END, '-' + g.name)
                        if codes_var.get() == 1:
                            text.insert(END, " -- ")
                            text.insert(END, ', '.join(g.codes))
                        text.insert(END, "\n")
                text.insert(END, "\n")
            text.config(state = DISABLED)
            show_missions_var = False

# ----------------- LONG MISSION GENERATION -----------------
        else:
            # random.seed(seed_value.get()) # allows unrandomized and randomized goals to be (almost) the same
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
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[i][rn1])-1)
                        mission = missions[i][rn1][rn2]
                        if rand_var.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        done = True

                    mission.def_num(i)
                    for c in mission.codes:
                        codes1.append(c)

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
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[rand_i][rn1])-1)
                        mission = missions[rand_i][rn1][rn2]
                        if rand_var.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        exists = False
                        for c in mission.codes:
                            if c in codes3:
                                exists = True
                                break
                        if exists: continue
                        done = True
                    # add mission's codes to list of codes
                    mission.def_num(rand_i)
                    for c in mission.codes:
                        if c in codes2:
                            codes3.append(c)
                        elif c in codes1:
                            codes2.append(c)
                        else:
                            codes1.append(c)
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
                short_main
            ],
            [ # EARLY_GAME
                mm,
                ttc,
                cc,
                fp,
                mmm
            ],
            [ # LATE_GAME
                gv,
                rbb,
                bgs,
                ccw
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
            for a,x in enumerate(missions):
                text.insert(END, short_label_list[a]+"\n")
                for c in x:
                    for g in c:
                        if rand_var.get() == 1: # if the checkbox is checked (don't randomize goals)
                            if g.rand == 1: continue # if the goal is random don't use it
                        else: # if the checkbox isn't checked (randomize goals)
                            if g.rand == 2: continue # if the goal is a nonrandom version of a random goal don't use it
                        text.insert(END, '-' + g.name)
                        if codes_var.get() == 1:
                            text.insert(END, " -- ")
                            text.insert(END, ', '.join(g.codes))
                        text.insert(END, "\n")
                text.insert(END, "\n")
            text.config(state = DISABLED)
            show_missions_var = False

# ----------------- SHORT MISSION GENERATION -----------------        
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
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[i][rn1])-1)
                        mission = missions[i][rn1][rn2]
                        if rand_var.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        done = True
                    
                    mission.def_num(i)
                    for c in mission.codes:
                        codes.append(c)

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
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[rand_i][rn1])-1)
                        mission = missions[rand_i][rn1][rn2]
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
                    mission.def_num(rand_i)
                    # comment this code below to enable repeating codes for early/late game
                    # if it's commented out that means codes can repeat for 2/3 (as long as they don't share 1's goal)
                    # vvvvvvvvvvvvvvvvvvvvvvv
                    # for c in mission.codes:
                    #     codes.append(c)
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

# --------------------------------------------------------------
# ----------------- MORE FUNCTIONS AND BUTTONS -----------------
# --------------------------------------------------------------
def mission_list():
    global show_missions_var
    show_missions_var = True
    main()

def show_settings():
    settings_win = Toplevel(win)
    settings_win.title("Settings")
    settings_win.grab_set()
    top_labelframe = LabelFrame(    settings_win, text = "Missions Generation")
    mid_labelframe = LabelFrame(    settings_win, text = "Display/Window Settings")
    bottom_labelframe = LabelFrame( settings_win, text = "Apply and Exit")

    top_labelframe.pack(    padx = 10, pady = 10, expand = TRUE, fill = BOTH)
    mid_labelframe.pack(    padx = 10, pady = 10, expand = TRUE, fill = BOTH)
    bottom_labelframe.pack( padx = 10, pady = 10, expand = TRUE, fill = BOTH)

    font_frame      = Frame(mid_labelframe)
    window_frame    = Frame(mid_labelframe)
    size_frame      = Frame(mid_labelframe)
    textbox_frame   = Frame(mid_labelframe)
    cleartext_frame = Frame(mid_labelframe)

    font_frame.pack(        padx = 10, pady = 5)
    window_frame.pack(      padx = 10, pady = 5)
    size_frame.pack(        padx = 10, pady = 5)
    textbox_frame.pack(     padx = 10, pady = 5)
    cleartext_frame.pack(   padx = 10, pady = 5)
    
    short_check         = Checkbutton(  top_labelframe,     font = default_font, text = "Short (if checked, short\nboard will be generated)", variable = short_var)
    codes_check         = Checkbutton(  top_labelframe,     font = default_font, text = "Show codes after each goal", variable = codes_var)
    rand_check          = Checkbutton(  top_labelframe,     font = default_font, text = "Unrandomize goals (by default,\ncertain goals are randomized)", variable = rand_var)
    font_size_label     = Label(        font_frame,         font = default_font, text = "Font size\n(default: 10)")
    font_size           = Entry(        font_frame,         textvariable = font_size_var, width = 8)
    win_size_label      = Label(        window_frame,       font = default_font, text = "Window size\n(default: 360x775)")
    win_size            = Entry(        window_frame,       textvariable = win_size_var, width = 18)
    current_size        = Button(       size_frame,         font = default_font, text = "Get current size/position", command = lambda: get_current_size(win_size))
    remove_text         = Button(       textbox_frame,      font = default_font, text = "Hide text boxes", command = lambda: remove_text_f(remove_text, show_text))
    show_text           = Button(       textbox_frame,      font = default_font, text = "Show text boxes", command = lambda: show_text_f(show_text, remove_text))
    clear_text          = Button(       cleartext_frame,    font = default_font, text = "Clear text boxes", command = clear_text_f)
    apply_settings      = Button(       bottom_labelframe,  font = default_font, text = "Apply settings", command = lambda: apply_settings_f(win_size, font_size))
    set_default         = Button(       bottom_labelframe,  font = default_font, text = "Set current values as defaults", command = set_default_f)
    new_quit            = Button(       bottom_labelframe,  font = default_font, text = "Exit settings", command = settings_win.destroy)

    short_check.pack(   padx = 10, pady = 5)
    codes_check.pack(   padx = 10, pady = 5)
    rand_check.pack(    padx = 10, pady = 5)

    font_size_label.grid(   row = 0, column = 0)
    font_size.grid(         row = 0, column = 1, padx = 10)
    win_size_label.grid(    row = 1, column = 0)
    win_size.grid(          row = 1, column = 1, padx = 10)
    current_size.grid(      row = 2, column = 1, padx = 10)
    remove_text.grid(       row = 3, column = 0, padx = 10)
    show_text.grid(         row = 3, column = 1, padx = 10)
    clear_text.grid(        row = 4, column = 0, columnspan = 2, padx = 10)

    apply_settings.pack(padx = 10, pady = 5)
    set_default.pack(padx = 10, pady = 5)
    new_quit.pack(padx = 10, pady = 5)

    if show_text_var.get() == 0:
        remove_text.config(state = DISABLED)
    else:
        show_text.config(state = DISABLED)
def copy():
    win.clipboard_clear()
    txt_to_copy = seed_value.get()
    if txt_to_copy != '':
        win.clipboard_append(txt_to_copy)

# ---------------------------------------------------
# ----------------- FINAL UI CONFIG -----------------
# ---------------------------------------------------

# -------------------- MAIN THREE BUTTONS AND SEED INPUT --------------------
gen_missions    = Button(top_frame, font = default_font, text = "Generate Missions",     command = main)
show_missions   = Button(top_frame, font = default_font, text = "Show list of missions", command = mission_list)
settings        = Button(top_frame, font = default_font, text = "Settings",              command = show_settings)
seed_frame      = Frame( top_frame)
gen_missions.grid(  row = 0, column = 3, pady = 6)
show_missions.grid( row = 1, column = 3, pady = 6)
settings.grid(      row = 2, column = 3, pady = 6)
seed_frame.grid(    row = 3, column = 3, pady = 6)


current_seed_box    = Entry(        seed_frame, font = default_font, textvariable = seed_value, state = DISABLED)
current_seed_label  = Label(        seed_frame, font = default_font, text = "Current Seed:")
current_seed_copy   = Button(       seed_frame, font = default_font, text = "Copy", command = copy)
custom_seed_box     = Entry(        seed_frame, font = default_font, textvariable = custom_seed_value)
custom_seed_label   = Label(        seed_frame, font = default_font, text = "Custom Seed:")
custom_seed_check   = Checkbutton(  seed_frame, variable = seed_var)
current_seed_box.grid(  row = 0, column = 2, pady = 6)
current_seed_label.grid(row = 0, column = 1, pady = 6)
current_seed_copy.grid( row = 0, column = 0, pady = 6)
custom_seed_box.grid(   row = 1, column = 2, pady = 6)
custom_seed_label.grid( row = 1, column = 1, pady = 6)
custom_seed_check.grid( row = 1, column = 0, pady = 6)

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

win.title("BK Missions Generator v3.2.1")
win.geometry(win_size_var.get())
win.minsize(170, 675)
win.mainloop()