# Original version by Trynan and Wedarobi
# Maintained by Trynan
# BK Missions idea by CrozB
# Mission generation logic and the missions themselves were come up with by CrozB
# 8/11/2020
# current: 6/23/2021

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import tkinter.ttk as ttk
from operator import attrgetter
import random
import configparser
import sys
import logging

# ---------------------------------------------------------
# -- SET UP LOGGING AND CONFIGURATION DEFAULTS

logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, filemode='w')

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press any key to exit.")
    sys.exit(-1)
sys.excepthook = show_exception_and_exit

CONFIG_ERROR = False
CONFIG = configparser.ConfigParser()
try:
    logging.info('reading bk_config.ini.')
    CONFIG.read('bk_config.ini')
    settings_section = CONFIG['settings'] # this is here to catch the error mostly
except:
    CONFIG_ERROR = True
    logging.warning('bk_config.ini not found. default settings will not be changeable.')

default_vals_list = []
logging.info('setting default values.')
if CONFIG_ERROR:
    # hard-code default values
    CONFIG = {
        'short':False,
        'show_codes':False,
        'unrandomize':False,
        'win_size':'360x775+148+156',
        'show_text':True,
        'font_size':'10'
    }
    for key in CONFIG:
        default_vals_list.append(CONFIG[key])
else:
    for key in CONFIG['settings']:
        default_vals_list.append(CONFIG['settings'][key])

class Mission:
    def __init__(self, rand, codes, name):
        self.rand = rand # 0 means normal, 1 means random, 2 means normal variant of a random goal
        self.codes = codes # list of codes, i.e. ["N", "A"]
        self.name = name # name of goal, i.e. "Open 765 note door"
    
    def def_num(self, num):
        self.num = num

# ---------------------------------------------------------
# -- WINDOW SETUP

logging.debug('setting up window and global variables.')
win = tk.Tk()

SHOW_MISSIONS = False
SHORT =             tk.BooleanVar()
SHOW_CODES =        tk.BooleanVar()
DONT_RANDOMIZE =    tk.BooleanVar()
SHOW_TEXT =         tk.BooleanVar()
USE_SEED =          tk.BooleanVar()
FONT_SIZE =         tk.IntVar() # positive integer
SEED_VALUE =        tk.StringVar() # six digit positive integer
WIN_SIZE =          tk.StringVar() # format: 360x675+100+1090 --> width x height + xoffset + yoffset
CUSTOM_SEED_VALUE = tk.StringVar()
VARIABLE_LIST = [SHORT, SHOW_CODES, DONT_RANDOMIZE, WIN_SIZE, SHOW_TEXT, FONT_SIZE]
LONG_LABEL_LIST = [
    "1. Main Objective",
    "2. Side Quest",
    "3. Early Game",
    "4. Mid Game",
    "5. Late Game"
]
SHORT_LABEL_LIST = [
    "1. Main Objective",
    "2. Early Game",
    "3. Late Game"
]
JINJO_LIST = [
    "purple",
    "green",
    "blue",
    "yellow",
    "orange"
]
# set all of these configuarables to their defaults as dictated by the config file
for i,val in enumerate(default_vals_list):
    VARIABLE_LIST[i].set(val)

# only doing this to change font size
default_font = tkFont.Font(family = 'TkTextFont', size = FONT_SIZE.get())

# ---------------------------------------------------------
# -- WIDGET INITIALIZATION

logging.debug('setting up widgets.')
top_frame = tk.Frame(win)
top_frame.grid(row = 0, column = 0, columnspan = 3)

b1t = tk.StringVar(value = "First Goal")
b2t = tk.StringVar(value = "Second Goal")
b3t = tk.StringVar(value = "Third Goal")
b4t = tk.StringVar(value = "Fourth Goal")
b5t = tk.StringVar(value = "Fifth Goal")
btextlist = [b1t, b2t, b3t, b4t, b5t]

b1 = tk.Button(win, command = lambda: cycle_color(b1))
b2 = tk.Button(win, command = lambda: cycle_color(b2))
b3 = tk.Button(win, command = lambda: cycle_color(b3))
b4 = tk.Button(win, command = lambda: cycle_color(b4))
b5 = tk.Button(win, command = lambda: cycle_color(b5))
blist = [b1, b2, b3, b4, b5]

t1 = tk.Text(win)
t2 = tk.Text(win)
t3 = tk.Text(win)
t4 = tk.Text(win)
t5 = tk.Text(win)
tlist = [t1, t2, t3, t4, t5]

s1 = tk.Scrollbar(win)
s2 = tk.Scrollbar(win)
s3 = tk.Scrollbar(win)
s4 = tk.Scrollbar(win)
s5 = tk.Scrollbar(win)
slist = [s1, s2, s3, s4, s5]

# ---------------------------------------------------------
# -- WIDGET INITIALIZATION

logging.debug('configuring widgets.')
for i,b in enumerate(blist):
    b.grid(row = i+5, column = 0, sticky = 'nsew')
    b.config(textvar = btextlist[i], bg = "White", width = 20, font = default_font)
    if not SHOW_TEXT.get():
        size = CONFIG['settings']['win_size'][:4]
        if 'x' in size: # number is 3 digits and not 4
            size = size[:3]
        b.config(wraplength = size)
    else:
        b.config(wraplength = 165)
if SHORT.get():
    b4t.set("-----")
    b5t.set("-----")
    b4.config(state = tk.DISABLED)
    b5.config(state = tk.DISABLED)

for i,t in enumerate(tlist):
    t.config(height = 7, width = 15, font = default_font)
    t.grid(row = i+5, column = 1, sticky='nsew')
    t['yscrollcommand'] = slist[i].set

for i,s in enumerate(slist):
    s.config(command = tlist[i].yview)
    s.grid(row = i+5, column = 2, sticky='nsew')

# ---------------------------------------------------------
# -- BUTTON FUNCTIONS

def cycle_color(b):
    """ b is button object, function cycles that button's background color from white -> green -> red -> white. """
    logging.info('cycling color of a button.')
    if b.cget('bg') == "White":
        b.config(bg = "Green", activebackground = "Green")
    elif b.cget('bg') == "Green":
        b.config(bg = "Red", activebackground = "Red")
    elif b.cget('bg') == "Red":
        b.config(bg = "White", activebackground = "White")

def get_current_size(t):
    """ function gets current size of window and puts it into t. """
    logging.info(f'getting current size which is {win.winfo_geometry()}')
    t.delete(0, tk.END)
    t.insert(tk.END, win.winfo_geometry())

def toggle_text_boxes():
    """ toggles the visibility of the text boxes. """
    logging.info('toggling visibility of text boxes.')
    current_state = SHOW_TEXT.get()
    desired_state = not current_state
    SHOW_TEXT.set(desired_state)
    if desired_state: # show text boxes
        for i in range(len(tlist)):
            # all these lists are the same length
            tlist[i].grid(row = i+5, column = 1, sticky = 'nsew')
            slist[i].grid(row = i+5, column = 2, sticky = 'nsew')
            blist[i].config(wraplength = 165)
    else: # remove text boxes
        for i in range(len(tlist)):
            tlist[i].grid_forget()
            slist[i].grid_forget()
            blist[i].config(wraplength = win.winfo_width())
    win.grid_columnconfigure(0, weight = int(current_state)) # 1 if removing, 0 if not
    win.grid_columnconfigure(1, weight = int(desired_state)) # 0 if removing, 1 if not

def clear_text_boxes():
    """ clears all text in the text boxes. """
    logging.info('clearing all text boxes.')
    for t in tlist:
        t.delete("1.0", tk.END)

def apply_settings(t1, t2):
    """ applies current settings. t1 (window size) and t2 (font size) are entry windows with needed text. """
    logging.info('applying settings.')
    global WIN_SIZE
    global FONT_SIZE
    new_win_size = t1.get()
    new_font_size = t2.get()
    WIN_SIZE.set(new_win_size)
    FONT_SIZE.set(new_font_size)
    default_font.config(size = new_font_size)
    win.geometry(new_win_size)
    # update wrapping on buttons (in case window size changed)
    for b in blist:
        if SHOW_TEXT.get():
            b.config(wraplength = 165)
        else:
            b.config(wraplength = win.winfo_width())

def set_default_settings():
    """ applies default settings into the config file. """
    logging.info('writing default settings into the config file.')
    if CONFIG_ERROR:
        messagebox.showerror('Config Missing!', 'Since your configuration file was not found on startup, default settings cannot be applied. Make sure you have a configuration file named "bk_config.ini" in the same directory as this file!')
        logging.debug('not writing default settings since no config file was found.')
        return
    for i,key in enumerate(CONFIG['settings']):
        CONFIG.set('settings', key, str(VARIABLE_LIST[i].get()))
    with open('bk_config.ini', 'w') as configfile:
        CONFIG.write(configfile)

# ---------------------------------------------------------
# -- HELPER FUNCTIONS

def set_seed():
    """ based on global seed variables, sets up all random seed stuff. """
    logging.debug('setting seed.')
    if USE_SEED.get(): # use custom seed
        SEED_VALUE.set(CUSTOM_SEED_VALUE.get())
        logging.info(f'using custom seed: {CUSTOM_SEED_VALUE.get()}')
        return SEED_VALUE.get()
    # get new random seed
    random.seed() # randomize current seed based on system time
    rn = random.randrange(100000, 1000000)
    SEED_VALUE.set(rn)
    CUSTOM_SEED_VALUE.set(rn)
    logging.info(f'using random seed: {rn}')
    return rn # this is new seed

def set_up_buttons():
    """ clears text boxes and resets text box backgrounds. """
    logging.info('resetting text and buttons.')
    clear_text_boxes()
    for b in blist: # set backgrounds back to white
        b.config(bg = "White")

def get_long_main():
    """ returns list of mission objects for the long main category. """
    return [
        Mission(0, ["N"],           "Open 765 note door"),
        Mission(0, ["O"],           "All Jinjos"),
        Mission(0, ["N"],           "Defeat Grunty"),
        Mission(0, ["H", "T"],      "All 24 honeycombs"),
        Mission(0, ["T"],           "All 116 tokens"),
        Mission(0, ["J"],           "Open all 9 worlds"),
        Mission(0, ["N", "R"],      "All notes"),
        Mission(1, ["J", "R"],      f"{random.randint(75,90)} jiggies [r 75-90]"),
        Mission(2, ["J", "R"],      "85 jiggies"),
        Mission(0, ["N", "J", "R"], "Open DoG & defeat Grunty"),
        Mission(0, ["J"],           "Humanitarian: Jiggies: Chimpy, Blubber, raise Clanker/fix both teeth, Tanktup, presents in FP, Gobi's rock, Trunker, Snorkel, Nabut, Eyrie.\nOthers (no jiggy): Gnawty's Boulder, Tooty"),
        Mission(0, ["N", "R"],      "Open All 12 Note Doors and Defeat Grunty"),
        Mission(0, ["A"],           "All of 1 type of collectible from each world (all tokens, honeycombs, notes, or jiggies, must do at least one of each in a unique world)"),
    ]

def get_long_side():
    """ returns list of mission objects for the long side category. """
    return [
        Mission(1, ["H", "A"],      f"{random.randint(14,18)} HCs [r 14-18]"),
        Mission(2, ["H", "A"],      "18 HCs"),
        Mission(0, ["T"],           "All 5 transformations"),
        Mission(0, [],              "All 10 Brentilda visits"),
        Mission(0, ["O"],           f"All 9 {JINJO_LIST[random.randint(0,4)]} Jinjos (color randomly chosen)"),
        Mission(0, ["N"],           "Open the 640 note door"),
        Mission(1, ["T"],           f"{random.randint(70,90)} tokens [r 70-90]"),
        Mission(2, ["T"],           "90 tokens"),
        Mission(1, ["J"],           f"{random.randint(40,60)} jiggies [r 40-60]"),
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

def get_short_main():
    """ returns list of mission objects for the short main category. """
    return [
        Mission(1, ["H"],           f"{random.randint(14,18)} HCs [r 14-18] "),
        Mission(2, ["H"],           "18 HCs"),
        Mission(0, ["T"],           "All 5 tranformations"),
        Mission(0, ["O"],           "All Jinjos of any 1 color (your choice)"),
        Mission(0, [],              "All 10 Brentilda visits"),
        Mission(0, ["N"],           "Open the 640 note door"),
        Mission(1, ["T"],           f"{random.randint(70,90)} tokens [r 70-90]"),
        Mission(2, ["T"],           "90 tokens"),
        Mission(1, ["J"],           f"{random.randint(45,60)} jiggies [r 45-60]"),
        Mission(2, ["J"],           "45 jiggies"),
        Mission(0, [],              "All 3 Cheato visits"),
        Mission(0, [],              "Activate all 8 warp cauldrons (not Dingpot)"),
        Mission(0, ["T"],           "Save Tooty"),
        Mission(0, ["J"],           "2 jiggies from each world"),
        Mission(0, ["J"],           "All lair jiggies"),
    ]

def get_levels():
    """ returns dictionary where keys are levels and values are lists of mission objects for the respective level category. """
    return {
        'mm':[
            Mission(0, ["R"],           "Begin run w/ MM 100% Trotless"),
            Mission(0, ["J", "R"],      "No more than 2 jiggies in MM"),
            Mission(0, [],              "Termite's Quest: 5 jiggies and 1 HC as the termite"),
        ],
        'ttc':[
            Mission(1, ["J", "A"],      f"{random.randint(8,10)} jiggies in TTC [r 8-10]"),
            Mission(2, ["J", "A"],      "All jiggies in TTC"),
            Mission(0, ["H", "A"],      "Both HCs in TTC"),
            Mission(0, ["T", "A"],      "All tokens in TTC"),
        ],
        'cc':[
            Mission(0, ["O", "A"],      "All Jinjos in CC"),
            Mission(1, ["J", "A"],      f"{random.randint(8,10)} jiggies in CC [r 8-10]"),
            Mission(2, ["J", "A"],      "All jiggies in CC"),
            Mission(1, ["N", "A"],      f"{random.randint(80,100)} notes in CC [r 80-100]"),
            Mission(2, ["N", "A"],      "All notes in CC"),
            Mission(0, ["H", "A"],      "Both HCs in CC"),
            Mission(0, ["J"],           "All 4 jiggies inside Clanker"),
        ],
        'fp':[
            Mission(0, ["O", "A"],      "All Jinjos in FP"),
            Mission(1, ["N", "A"],      f"{random.randint(80,100)} notes in FP [r 80-100]"),
            Mission(2, ["N", "A"],      "All notes in FP"),
            Mission(0, ["H", "A"],      "Both HCs in FP"),
            Mission(0, ["T", "A"],      "All tokens in FP"),
            Mission(0, ["J"],           "Merry Christmas! (Visit Boggy's igloo w/ him in it & give presents)"),
            Mission(1, ["J", "A"],      f"{random.randint(4,9)} jiggies in FP [r 4-9]"),
            Mission(2, ["J", "A"],      "9 jiggies in FP"),	
        ],
        'mmm':[
            Mission(0, ["O", "A"],      "All Jinjos in MMM"),
            Mission(1, ["J", "A"],      f"{random.randint(6,10)} jiggies in MMM [r 6-10]"),
            Mission(2, ["J", "A"],      "All jiggies in MMM"),
            Mission(1, ["N", "A"],      f"{random.randint(60,100)} notes in MMM [r 60-100]"),
            Mission(2, ["N", "A"],      "All notes in MMM"),
            Mission(0, ["H", "A"],      "Both HCs in MMM"),
            Mission(1, ["T", "A"],      f"{random.randint(10,16)} tokens in MMM [r 10-16]"),
            Mission(2, ["T", "A"],      "All (16) tokens in MMM"),
            Mission(0, [],              "MMM witch switch jiggy"),
            Mission(0, [],              "Kill all 10 Limbos (skeletons) in MMM"),
        ],
        'gv':[
            Mission(0, ["O", "A"],      "All Jinjos in GV"),
            Mission(1, ["N", "A"],      f"{random.randint(40,100)} notes in GV [r 40-100]"),
            Mission(2, ["N", "A"],      "All notes in GV"),
            Mission(0, ["H", "A"],      "Both HCs in GV"),
            Mission(0, ["T", "A"],      "All tokens in GV"),
            Mission(0, [],              "GV rings jiggy without flight or bee"),
            Mission(1, ["J", "A"],      f"{random.randint(4,9)} jiggies in GV [r 4-9]"),
            Mission(2, ["J", "A"],      "9 Jiggies in GV"),
            Mission(0, ["J"],           "Abuse Gobi (beak bust Gobi at all 5 locations)"),
        ],
        'rbb':[
            Mission(0, ["O", "A"],      "All Jinjos in RBB"),
            Mission(1, ["J", "A"],      f"{random.randint(4,10)} jiggies in RBB [r 4-10]"),
            Mission(2, ["J", "A"],      "All jiggies in RBB"),
            Mission(1, ["N", "A"],      f"{random.randint(40,100)} notes in RBB [r 40-100]"),
            Mission(2, ["N", "A"],      "All notes in RBB"),
            Mission(0, ["H", "A"],      "Both HCs in RBB"),
            Mission(1, ["T", "A"],      f"{random.randint(10,15)} tokens in RBB [r 10-15]"),
            Mission(2, ["T", "A"],      "All tokens in RBB"),
        ],
        'ccw':[
            Mission(0, ["O", "A"],      "All Jinjos in CCW"),
            Mission(0, ["H", "A"],      "Both HCs in CCW"),
            Mission(0, [],              "All 21 caterpillars"),
            Mission(0, [],              "Eyrie's jiggy"),
            Mission(0, ["J"],           "Nabnut's jiggy"),
            Mission(0, [],              "Kill all 6 Sir Slushes in winter"),
            Mission(0, ["J"],           "Flower jiggy in CCW"),
            Mission(1, ["N", "A"],      f"{random.randint(50,80)} notes in CCW [r 50-80]"),
            Mission(2, ["N", "A"],      "80 notes in CCW"),
            Mission(1, ["J", "A"],      f"{random.randint(4,8)} jiggies in CCW [r 4-8]"),
            Mission(2, ["J", "A"],      "8 jiggies in CCW"),
            Mission(1, ["T", "A"],      f"{random.randint(15,25)} tokens in CCW [r 15-25]"),
            Mission(2, ["T", "A"],      "20 tokens in CCW"),
            Mission(0, ["J", "T", "R"], "Collect 8 jiggies as the bee"),
        ],
        'bgs':[
            Mission(0, ["O", "A"],      "All Jinjos in BGS"),
            Mission(1, ["N", "A"],      f"{random.randint(75,100)} notes in BGS [r 75-100]"),
            Mission(2, ["N", "A"],      "All notes in BGS"),
            Mission(0, ["H", "A"],      "Both HCs in BGS"),
            Mission(0, ["T", "A"],      "All tokens in BGS"),
            Mission(0, ["J"],           "Croctuses jiggy"),
            Mission(0, ["J"],           "Tiptup's jiggy"),
            Mission(0, ["J"],           "Both timed jiggies in BGS"),
            Mission(1, ["J"],           f"{random.randint(5,8)} jiggies in BGS [r 5-8]"),
            Mission(2, ["J"],           "9 jiggies in BGS"),
        ],
    }

def show_missions(missions):
    """ make a toplevel window containing a list of all the missions (long/short depending on that variable). """
    logging.info('showing missions.')
    global SHOW_MISSIONS
    new_win = tk.Toplevel(win)
    new_win.grab_set()
    new_win.title("Missions List")
    text = tk.Text(new_win, font = default_font)
    scroll = tk.Scrollbar(new_win, command = text.yview)
    text['yscrollcommand'] = scroll.set
    text.grid(row = 0, column = 0, sticky = 'nsew')
    scroll.grid(row = 0, column = 1, sticky = 'nsew')
    new_win.grid_columnconfigure(0, weight = 1)
    new_win.grid_rowconfigure(0, weight = 1)

    label_list = [LONG_LABEL_LIST, SHORT_LABEL_LIST]
    text_list = ["LONG", "SHORT"]
    text.config(state = tk.NORMAL)
    text.delete("1.0", tk.END)
    text.insert(tk.END, f"LIST OF {text_list[int(SHORT.get())]} MISSIONS:\n\n")
    for label_num, category in enumerate(missions):
        text.insert(tk.END, LONG_LABEL_LIST[label_num] + '\n')
        for l in category: # category is a list of lists
            for goal in l: # go through each goal in the sub-lists
                if DONT_RANDOMIZE.get():
                    if goal.rand == 1: continue # don't use random goals
                else:
                    if goal.rand == 2: continue # don't use nonrandom versions of random goals
                text.insert(tk.END, '-' + goal.name)
                if SHOW_CODES.get():
                    text.insert(tk.END, ' -- ' + ', '.join(goal.codes))
                text.insert(tk.END, '\n')
        # end of category
        text.insert(tk.END, '\n')
    text.config(state = tk.DISABLED)
    SHOW_MISSIONS = False

def random_mission(missions_list, codes):
    """ get a random mission from sub-list missions_list while excluding codes that are in the codes list. """
    count = len(missions_list)
    done = False
    while not done:
        rn1 = random.randrange(0, count)
        rn2 = random.randrange(0, len(missions_list[rn1]))
        mission = missions_list[rn1][rn2]
        if DONT_RANDOMIZE.get(): # exclude randoms
            if mission.rand == 1: continue
        else: # exclude nonrandoms
            if mission.rand == 2: continue
        # search for conflicting codes
        exists = False
        for c in mission.codes: 
            if c in codes:
                exists = True
                break
        if exists: continue
        done = True
    logging.info(f'mission found: {mission.name} with codes {mission.codes} and randomness {mission.rand}.')
    return mission
        
def write_sorted_goals(sorted_goals):
    """ writes goals onto the buttons. """
    for i,g in enumerate(sorted_goals):
        if SHOW_CODES.get():
            btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
        else:
            btextlist[i].set(g.name)

def get_random_i(length, i_list):
    """ gets a random i based on length (int) which isn't in i_list. """
    rand_i = random.randrange(1, length)
    while rand_i in i_list:
        rand_i = random.randrange(1, length)
    i_list.append(rand_i)
    return rand_i

def generate_goals(missions):
    logging.info('generating goals.')
    short = SHORT.get()
    if short:
        b4t.set("-----")
        b5t.set("-----")
        b4.config(state = tk.DISABLED)
        b5.config(state = tk.DISABLED)
    else:
        b4.config(state = tk.NORMAL)
        b5.config(state = tk.NORMAL)
    goals = []
    codes1 = []
    codes2 = [] # intermediary
    codes3 = [] # if codes are present twice, then remove them
    i_list = []

    for i in range(len(missions)):
        if not i:
            rand_i = 0
            mission = random_mission(missions[i], codes3)
        else:
            # after i = 0 do them randomly
            rand_i = get_random_i(len(missions), i_list)
            mission = random_mission(missions[rand_i], codes3)
        
        mission.def_num(rand_i)
        if short and not i: # exclude codes from short main category, but no other short categories
            for c in mission.codes:
                codes3.append(c)
        elif not short:
            for c in mission.codes:
                if c in codes2: codes3.append(c)
                elif c in codes1: codes2.append(c)
                else: codes1.append(c)
        goals.append(mission)
    goals_sorted = sorted(goals, key=attrgetter('num'))
    # write the goals to the buttons
    write_sorted_goals(goals_sorted)


# ---------------------------------------------------------
# -- OTHER FUNCTIONS AND BUTTONS
def mission_list():
    global SHOW_MISSIONS
    SHOW_MISSIONS = True
    main()

def copy():
    logging.info('copying.')
    win.clipboard_clear()
    txt_to_copy = SEED_VALUE.get()
    if txt_to_copy:
        win.clipboard_append(txt_to_copy)

def show_settings():
    logging.info('opening settings.')
    settings_win = tk.Toplevel(win)
    settings_win.grab_set()
    settings_win.title("Settings")
    top_labelframe = tk.LabelFrame(settings_win, text = "Missions Generation")
    mid_labelframe = tk.LabelFrame(settings_win, text = "Display/Window Settings")
    bottom_labelframe = tk.LabelFrame(settings_win, text = "Apply and Exit")

    top_labelframe.pack(    padx = 10, pady = 10, expand = tk.TRUE, fill = tk.BOTH)
    mid_labelframe.pack(    padx = 10, pady = 10, expand = tk.TRUE, fill = tk.BOTH)
    bottom_labelframe.pack( padx = 10, pady = 10, expand = tk.TRUE, fill = tk.BOTH)

    font_frame      = tk.Frame(mid_labelframe)
    window_frame    = tk.Frame(mid_labelframe)
    others_frame    = tk.Frame(mid_labelframe)

    font_frame.pack(    padx = 10, pady = 5)
    window_frame.pack(  padx = 10, pady = 5)
    others_frame.pack(  padx = 10, pady = 5)

    short_check         = tk.Checkbutton(top_labelframe,     font = default_font, text = "Short (if checked, short\nboard will be generated)", variable = SHORT)
    codes_check         = tk.Checkbutton(top_labelframe,     font = default_font, text = "Show codes after each goal", variable = SHOW_CODES)
    rand_check          = tk.Checkbutton(top_labelframe,     font = default_font, text = "Unrandomize goals (by default,\ncertain goals are randomized)", variable = DONT_RANDOMIZE)
    font_size_label     = tk.Label(      font_frame,         font = default_font, text = "Font size\n(default: 10)")
    font_size           = tk.Entry(      font_frame,         textvariable = FONT_SIZE, width = 8)
    win_size_label      = tk.Label(      window_frame,       font = default_font, text = "Window size\n(default: 360x775)")
    win_size            = tk.Entry(      window_frame,       textvariable = WIN_SIZE, width = 18)
    current_size        = tk.Button(     others_frame,       font = default_font, text = "Get current size/position", command = lambda: get_current_size(win_size))
    toggle_text         = tk.Button(     others_frame,       font = default_font, text = "Toggle text boxes", command = toggle_text_boxes)
    clear_text          = tk.Button(     others_frame,       font = default_font, text = "Clear text boxes", command = clear_text_boxes)
    apply_settings_btn  = tk.Button(     bottom_labelframe,  font = default_font, text = "Apply settings", command = lambda: apply_settings(win_size, font_size))
    set_default         = tk.Button(     bottom_labelframe,  font = default_font, text = "Set current values as defaults", command = set_default_settings)
    new_quit            = tk.Button(     bottom_labelframe,  font = default_font, text = "Exit settings", command = settings_win.destroy)

    short_check.pack(   padx = 10, pady = 5)
    codes_check.pack(   padx = 10, pady = 5)
    rand_check.pack(    padx = 10, pady = 5)

    font_size_label.grid(   row = 0, column = 0)
    font_size.grid(         row = 0, column = 1, padx = 10)
    win_size_label.grid(    row = 0, column = 0)
    win_size.grid(          row = 0, column = 1, padx = 10)
    current_size.grid(      row = 0, column = 0, pady = 5)
    toggle_text.grid(       row = 1, column = 0, pady = 5)
    clear_text.grid(        row = 2, column = 0, pady = 5)

    apply_settings_btn.pack(padx = 10, pady = 5)
    set_default.pack(padx = 10, pady = 5)
    new_quit.pack(padx = 10, pady = 5)

# ---------------------------------------------------------
# ---------------------------------------------------------
# -- MAIN FUNCTIONALITY
def main():
    """ main function, gets a set of missions randomly based on certain restrictions. """
    logging.info('entering main.')
    random.seed(str(set_seed()))
    set_up_buttons()
    # we have to get the list of missions every time so that the randomized ones are different every time.
    # this is also why the show_missions function is in here, because it needs to use the full list of missions.
    long_main = get_long_main()
    long_side = get_long_side()
    short_main = get_short_main()
    levels = get_levels()

    if not SHORT.get():
        missions = [
            [long_main], # MAIN_OBJECTIVE
            [long_side], # SIDE_QUEST
            [ # EARLY_GAME
                levels['mm'],
                levels['ttc'],
                levels['cc'],
                levels['fp']
            ],
            [ # MID_GAME
                levels['mmm'],
                levels['gv'],
                levels['rbb']
            ],
            [ # LATE_GAME
                levels['bgs'],
                levels['ccw']
            ]
        ]
    else:
        missions = [
            [short_main],
            [ # EARLY_GAME
                levels['mm'],
                levels['ttc'],
                levels['cc'],
                levels['fp'],
                levels['mmm']
            ],
            [ # LATE_GAME
                levels['gv'],
                levels['rbb'],
                levels['bgs'],
                levels['ccw']
            ]
        ]
    if SHOW_MISSIONS:
        show_missions(missions)
    else: # generate long missions
        generate_goals(missions)
    logging.info('exiting main.')

# ---------------------------------------------------------
# -- FINAL UI CONFIG

logging.info('doing final ui configurations.')
gen_missions        = tk.Button(top_frame, font = default_font, text = "Generate Missions",     command = main)
show_missions_btn   = tk.Button(top_frame, font = default_font, text = "Show list of missions", command = mission_list)
settings            = tk.Button(top_frame, font = default_font, text = "Settings",              command = show_settings)
seed_frame          = tk.Frame( top_frame)
gen_missions.grid(  row = 0, column = 3, pady = 6)
show_missions_btn.grid( row = 1, column = 3, pady = 6)
settings.grid(      row = 2, column = 3, pady = 6)
seed_frame.grid(    row = 3, column = 3, pady = 6)

current_seed_box    = tk.Entry(        seed_frame, font = default_font, textvariable = SEED_VALUE, state = tk.DISABLED)
current_seed_label  = tk.Label(        seed_frame, font = default_font, text = "Current Seed:")
current_seed_copy   = tk.Button(       seed_frame, font = default_font, text = "Copy", command = copy)
custom_seed_box     = tk.Entry(        seed_frame, font = default_font, textvariable = CUSTOM_SEED_VALUE)
custom_seed_label   = tk.Label(        seed_frame, font = default_font, text = "Custom Seed:")
custom_seed_check   = tk.Checkbutton(  seed_frame, variable = USE_SEED)
current_seed_box.grid(  row = 0, column = 2, pady = 6)
current_seed_label.grid(row = 0, column = 1, pady = 6)
current_seed_copy.grid( row = 0, column = 0, pady = 6)
custom_seed_box.grid(   row = 1, column = 2, pady = 6)
custom_seed_label.grid( row = 1, column = 1, pady = 6)
custom_seed_check.grid( row = 1, column = 0, pady = 6)

win.grid_columnconfigure(1, weight = 1)
for i in range(5, 10):
    win.grid_rowconfigure(i, weight = 1)

if not CONFIG_ERROR and CONFIG['settings']['show_text'] == '0':
    toggle_text_boxes()

win.title("BK Missions Generator v3.3")
win.geometry(WIN_SIZE.get())
win.minsize(300, 675)
if CONFIG_ERROR:
    messagebox.showerror('Config Missing!', "Oops! I couldn't find your configuration file (bk_config.ini). Make sure it's in this folder and you didn't change its name. In the meantime, you can continue but you won't be able to change default values.")
logging.info('done with all setup.')
win.mainloop()