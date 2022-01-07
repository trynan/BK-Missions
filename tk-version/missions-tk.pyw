# Original version by Trynan and Wedarobi
# Maintained by Trynan
# BK Missions idea by CrozB
# Mission generation logic and the missions themselves were come up with by CrozB
# 8/11/2020
# current: 1/06/2022

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import random
import configparser
import sys
import logging

import generation
from generation import Mission

# ---------------------------------------------------------
# -- SET UP LOGGING AND CONFIGURATION DEFAULTS

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press any key to exit.")
    sys.exit(-1)

logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, filemode='w')
sys.excepthook = show_exception_and_exit
CONFIG = configparser.ConfigParser()
CONFIG_ERROR = False

logging.info('reading bk_config.ini.')
CONFIG.read('bk_config.ini')
try:
    # make sure the correct config file was found
    settings_section = CONFIG['settings']
except KeyError:
    CONFIG_ERROR = True
    logging.warning('bk_config.ini not found. default settings will not be changeable.')

default_vals_list = []
logging.info('setting default values.')
if CONFIG_ERROR:
    # hard-code default values if there was an error with the config file
    CONFIG = {
        'short': False,
        'show_codes': False,
        'unrandomize': False,
        'win_size': '360x775+148+156',
        'show_text': True,
        'font_size': '10'
    }
    for key in CONFIG:
        default_vals_list.append(CONFIG[key])
else:
    for key in CONFIG['settings']:
        default_vals_list.append(CONFIG['settings'][key])


# ---------------------------------------------------------
# -- WINDOW SETUP

logging.debug('setting up window and global variables.')
win = tk.Tk()

SHOW_MISSIONS = False
SHORT = tk.BooleanVar()
SHOW_CODES = tk.BooleanVar()
DONT_RANDOMIZE = tk.BooleanVar()
SHOW_TEXT = tk.BooleanVar()
USE_SEED = tk.BooleanVar()
FONT_SIZE = tk.IntVar()  # positive integer
SEED_VALUE = tk.StringVar()  # six digit positive integer
# format: "360x675+100+1090" --> width x height + xoffset + yoffset
WIN_SIZE = tk.StringVar()
CUSTOM_SEED_VALUE = tk.StringVar()
VARIABLE_LIST = [SHORT, SHOW_CODES, DONT_RANDOMIZE, WIN_SIZE, SHOW_TEXT, FONT_SIZE]
# set all of these configuarables to their defaults as dictated by the config file
try:
    logging.info('writing default values into variables.')
    for i, val in enumerate(default_vals_list):
        VARIABLE_LIST[i].set(val)
except:
    logging.error(f'there was an issue with the configuration file. here is what was inside: {[k for k in default_vals_list]}')
    messagebox.showerror('Configuration Error', 'There was an issue with the configuration file. Please make sure your configuration file has valid inputs.\nValid inputs are\nshort: True/False\nshow_codes: True/False\nunrandomize: True/False\nwin_size: 360x775+193+73 (width x height + xoffset + yoffset)\nshow_text: True/False\nfont_size: any positive integer (default is 10).')
    sys.exit(-1)

# only doing this to change font size
default_font = tkFont.Font(family='TkTextFont', size=FONT_SIZE.get())

# ---------------------------------------------------------
# -- WIDGET INITIALIZATION

logging.debug('setting up widgets.')
top_frame = tk.Frame(win)
top_frame.grid(row=0, column=0, columnspan=3)

b1t = tk.StringVar(value="First Goal")
b2t = tk.StringVar(value="Second Goal")
b3t = tk.StringVar(value="Third Goal")
b4t = tk.StringVar(value="Fourth Goal")
b5t = tk.StringVar(value="Fifth Goal")
btextlist = [b1t, b2t, b3t, b4t, b5t]

# using lambdas here in order to pass in arguments
b1 = tk.Button(win, command=lambda: cycle_color(b1))
b2 = tk.Button(win, command=lambda: cycle_color(b2))
b3 = tk.Button(win, command=lambda: cycle_color(b3))
b4 = tk.Button(win, command=lambda: cycle_color(b4))
b5 = tk.Button(win, command=lambda: cycle_color(b5))
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
for i, b in enumerate(blist):
    b.grid(row=i+5, column=0, sticky='nsew')
    b.config(textvar=btextlist[i], bg="White", width=20, font=default_font)
    if not SHOW_TEXT.get():
        size = CONFIG['settings']['win_size'][:4]
        if 'x' in size:  # number is 3 digits and not 4
            size = size[:3]
        b.config(wraplength=size)
    else:
        b.config(wraplength=165)
if SHORT.get():
    b4t.set("-----")
    b5t.set("-----")
    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)

for i, t in enumerate(tlist):
    t.config(height=7, width=15, font=default_font)
    t.grid(row=i+5, column=1, sticky='nsew')
    t['yscrollcommand'] = slist[i].set

for i, s in enumerate(slist):
    s.config(command=tlist[i].yview)
    s.grid(row=i+5, column=2, sticky='nsew')

# ---------------------------------------------------------
# -- BUTTON FUNCTIONS

def cycle_color(b):
    """
    Cycles through white -> green -> red, changing the given button's background color.
    - b is a tkinter button widget.
    """
    logging.info('cycling color of a button.')
    if b.cget('bg') == "White":
        b.config(bg="Green", activebackground="Green")
    elif b.cget('bg') == "Green":
        b.config(bg="Red", activebackground="Red")
    elif b.cget('bg') == "Red":
        b.config(bg="White", activebackground="White")


def get_current_win_size(t):
    """
    Gets the current size of the main window and puts it into the given text box.
    - t is a tkinter text (or entry) widget.
    """
    logging.info(f'getting current size which is {win.winfo_geometry()}')
    t.delete(0, tk.END)
    t.insert(tk.END, win.winfo_geometry())


def toggle_text_boxes():
    """
    Toggles the visibility of the text boxes next to the buttons in the main window.
    """
    logging.info('toggling visibility of text boxes.')
    current_state = SHOW_TEXT.get()
    desired_state = not current_state
    SHOW_TEXT.set(desired_state)
    if desired_state:  # show text boxes
        for i in range(len(tlist)):
            # all these lists are the same length
            tlist[i].grid(row=i+5, column=1, sticky='nsew')
            slist[i].grid(row=i+5, column=2, sticky='nsew')
            blist[i].config(wraplength=165)
    else:  # remove text boxes
        for i in range(len(tlist)):
            tlist[i].grid_forget()
            slist[i].grid_forget()
            blist[i].config(wraplength=win.winfo_width())
    win.grid_columnconfigure(0, weight=int(current_state))  # 1 if removing, 0 if not
    win.grid_columnconfigure(1, weight=int(desired_state))  # 0 if removing, 1 if not


def clear_text_boxes():
    """
    Clears all text from the text boxes next to the buttons in the main window.
    """
    logging.info('clearing all text boxes.')
    for t in tlist:
        t.delete("1.0", tk.END)


def apply_settings(text_1, text_2):
    """
    Applies current settings.
    - t1 and t2 are tkinter entry widgets containing text used
      when applying settings.
    """
    logging.info('applying settings.')
    global WIN_SIZE
    global FONT_SIZE
    new_win_size = text_1.get()
    new_font_size = text_2.get()
    WIN_SIZE.set(new_win_size)
    FONT_SIZE.set(new_font_size)
    default_font.config(size=new_font_size)
    win.geometry(new_win_size)
    # update wrapping on buttons (in case window size changed)
    for b in blist:
        if SHOW_TEXT.get():
            b.config(wraplength=165)
        else:
            b.config(wraplength=win.winfo_width())


def set_default_settings():
    """ 
    Sets current settings as default by updating the configuration file.
    """
    logging.info('writing default settings into the config file.')
    if CONFIG_ERROR:
        messagebox.showerror('Config Missing!', 'Since your configuration file was not found on startup, default settings cannot be applied. Make sure you have a configuration file named "bk_config.ini" in the same directory as this file!')
        logging.debug('not writing default settings since no config file was found.')
        return
    for i, key in enumerate(CONFIG['settings']):
        CONFIG.set('settings', key, str(VARIABLE_LIST[i].get()))
    with open('bk_config.ini', 'w') as configfile:
        CONFIG.write(configfile)

# ---------------------------------------------------------
# -- HELPER FUNCTIONS

def set_seed():
    """ Sets up random seed stuff for the main function.
        If using custom seed, returns that seed.
        Otherwise, generates a new seed based on system time
        and returns that.
        - return: Random seed, should be an int or a string (usually
          of numbers, but actual strings can work too).
    """
    logging.debug('setting seed.')
    if USE_SEED.get():  # use custom seed
        SEED_VALUE.set(CUSTOM_SEED_VALUE.get())
        logging.info(f'using custom seed: {CUSTOM_SEED_VALUE.get()}')
        return SEED_VALUE.get()
    # get new random seed
    random.seed()  # randomize current seed based on system time
    rn = random.randrange(100000, 1000000)
    SEED_VALUE.set(rn)
    CUSTOM_SEED_VALUE.set(rn)
    logging.info(f'using random seed: {rn}')
    return rn  # this is new seed


def set_up_buttons():
    """
    Sets up the buttons for new mission generation by clearing
    all text boxes and resetting backgrounds of buttons.
    """
    logging.info('resetting text and buttons.')
    clear_text_boxes()
    for b in blist:  # set backgrounds back to white
        b.config(bg="White")


def write_sorted_goals(sorted_goals):
    """
    Prints the sorted goals onto the buttons.
    - sorted_goals is a list of either five or three mission objects.
    """
    for i, g in enumerate(sorted_goals):
        if SHOW_CODES.get():
            btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
        else:
            btextlist[i].set(g.name)


# ---------------------------------------------------------
# -- OTHER FUNCTIONS AND BUTTONS

def mission_list():
    # this has to be a separate function which calls main
    # because the mission lists are created in main
    global SHOW_MISSIONS
    SHOW_MISSIONS = True
    main()


def copy():
    logging.info('copying seed.')
    win.clipboard_clear()
    txt_to_copy = SEED_VALUE.get()
    if txt_to_copy:
        win.clipboard_append(txt_to_copy)


def show_settings():
    """
    Create and open a toplevel window for changing various settings.
    """
    logging.info('opening settings.')
    settings_win = tk.Toplevel(win)
    settings_win.grab_set()
    settings_win.title("Settings")
    top_labelframe = tk.LabelFrame(settings_win, text="Missions Generation")
    mid_labelframe = tk.LabelFrame(settings_win, text="Display/Window Settings")
    bottom_labelframe = tk.LabelFrame(settings_win, text="Apply and Exit")

    top_labelframe.pack(padx=10, pady=10, expand=tk.TRUE, fill=tk.BOTH)
    mid_labelframe.pack(padx=10, pady=10, expand=tk.TRUE, fill=tk.BOTH)
    bottom_labelframe.pack(padx=10, pady=10, expand=tk.TRUE, fill=tk.BOTH)

    font_frame = tk.Frame(mid_labelframe)
    window_frame = tk.Frame(mid_labelframe)
    others_frame = tk.Frame(mid_labelframe)

    font_frame.pack(padx=10, pady=5)
    window_frame.pack(padx=10, pady=5)
    others_frame.pack(padx=10, pady=5)

    short_check = tk.Checkbutton(top_labelframe, font=default_font, text="Short (if checked, short\nboard will be generated)", variable=SHORT)
    codes_check = tk.Checkbutton(top_labelframe, font=default_font, text="Show codes after each goal", variable=SHOW_CODES)
    rand_check = tk.Checkbutton(top_labelframe,  font=default_font, text="Unrandomize goals (by default,\ncertain goals are randomized)", variable=DONT_RANDOMIZE)
    font_size_label = tk.Label(font_frame, font=default_font, text="Font size\n(default: 10)")
    font_size = tk.Entry(font_frame, textvariable=FONT_SIZE, width=8)
    win_size_label = tk.Label(window_frame, font=default_font, text="Window size\n(default: 360x775)")
    win_size = tk.Entry(window_frame, textvariable=WIN_SIZE, width=18)
    current_size = tk.Button(others_frame, font=default_font, text="Get current size/position", command=lambda: get_current_win_size(win_size))
    toggle_text = tk.Button(others_frame, font=default_font, text="Toggle text boxes", command=toggle_text_boxes)
    clear_text = tk.Button(others_frame, font=default_font, text="Clear text boxes", command=clear_text_boxes)
    apply_settings_btn = tk.Button(bottom_labelframe,  font=default_font, text="Apply settings", command=lambda: apply_settings(win_size, font_size))
    set_default = tk.Button(bottom_labelframe,  font=default_font, text="Set current values as defaults", command=set_default_settings)
    new_quit = tk.Button(bottom_labelframe,  font=default_font, text="Exit settings", command=settings_win.destroy)

    short_check.pack(padx=10, pady=5)
    codes_check.pack(padx=10, pady=5)
    rand_check.pack(padx=10, pady=5)

    font_size_label.grid(row=0, column=0)
    font_size.grid(row=0, column=1, padx=10)
    win_size_label.grid(row=0, column=0)
    win_size.grid(row=0, column=1, padx=10)
    current_size.grid(row=0, column=0, pady=5)
    toggle_text.grid(row=1, column=0, pady=5)
    clear_text.grid(row=2, column=0, pady=5)

    apply_settings_btn.pack(padx=10, pady=5)
    set_default.pack(padx=10, pady=5)
    new_quit.pack(padx=10, pady=5)

# ---------------------------------------------------------
# ---------------------------------------------------------
# -- MAIN FUNCTIONALITY

def main():
    """
    Gets a set of missions randomly based on certain restrictions and
    prints the result onto the buttons in the main window.
    """
    logging.info('entering main.')
    global SHOW_MISSIONS
    random.seed(str(set_seed()))
    set_up_buttons()
    # we have to get the list of missions every time so that the randomized ones are different every time.
    # this is also why the show_missions function is in here, because it needs to use the full list of missions.
    long_main = generation.get_long_main()
    long_side = generation.get_long_side()
    short_main = generation.get_short_main()
    levels = generation.get_levels()

    if not SHORT.get():
        missions = [
            [long_main],  # MAIN_OBJECTIVE
            [long_side],  # SIDE_QUEST
            [  # EARLY_GAME
                levels['mm'],
                levels['ttc'],
                levels['cc'],
                levels['fp']
            ],
            [  # MID_GAME
                levels['mmm'],
                levels['gv'],
                levels['rbb']
            ],
            [  # LATE_GAME
                levels['bgs'],
                levels['ccw']
            ]
        ]
    else:
        missions = [
            [short_main],
            [  # EARLY_GAME
                levels['mm'],
                levels['ttc'],
                levels['cc'],
                levels['fp'],
                levels['mmm']
            ],
            [  # LATE_GAME
                levels['gv'],
                levels['rbb'],
                levels['bgs'],
                levels['ccw']
            ]
        ]
    if SHOW_MISSIONS:
        logging.info('showing missions list.')
        generation.show_missions(missions, SHORT.get(), DONT_RANDOMIZE.get(), SHOW_CODES.get())
        SHOW_MISSIONS = False
    else:
        logging.info('generating goals.')
        if SHORT.get():
            b4t.set("-----")
            b5t.set("-----")
            b4.config(state=tk.DISABLED)
            b5.config(state=tk.DISABLED)
        else:
            b4.config(state=tk.NORMAL)
            b5.config(state=tk.NORMAL)
        goals = generation.generate_goals(missions, SHORT.get(), DONT_RANDOMIZE.get())
        for m in goals:
            logging.info(f'mission found: {m.name} with codes {m.codes} and randomness {m.rand}.')
        write_sorted_goals(goals)
    logging.info('exiting main.')

# ---------------------------------------------------------
# -- FINAL UI CONFIG

logging.info('doing final ui configurations.')
gen_missions = tk.Button(top_frame, font=default_font, text="Generate Missions", command=main)
show_missions_btn = tk.Button(top_frame, font=default_font, text="Show list of missions", command=mission_list)
settings = tk.Button(top_frame, font=default_font, text="Settings", command=show_settings)
seed_frame = tk.Frame(top_frame)
gen_missions.grid(row=0, column=3, pady=6)
show_missions_btn.grid(row=1, column=3, pady=6)
settings.grid(row=2, column=3, pady=6)
seed_frame.grid(row=3, column=3, pady=6)

current_seed_box = tk.Entry(seed_frame, font=default_font, textvariable=SEED_VALUE, state=tk.DISABLED)
current_seed_label = tk.Label(seed_frame, font=default_font, text="Current Seed:")
current_seed_copy = tk.Button(seed_frame, font=default_font, text="Copy", command=copy)
custom_seed_box = tk.Entry(seed_frame, font=default_font, textvariable=CUSTOM_SEED_VALUE)
custom_seed_label = tk.Label(seed_frame, font=default_font, text="Custom Seed:")
custom_seed_check = tk.Checkbutton(seed_frame, variable=USE_SEED)
current_seed_box.grid(row=0, column=2, pady=6)
current_seed_label.grid(row=0, column=1, pady=6)
current_seed_copy.grid(row=0, column=0, pady=6)
custom_seed_box.grid(row=1, column=2, pady=6)
custom_seed_label.grid(row=1, column=1, pady=6)
custom_seed_check.grid(row=1, column=0, pady=6)

win.grid_columnconfigure(1, weight=1)
for i in range(5, 10):
    win.grid_rowconfigure(i, weight=1)

if not CONFIG_ERROR and CONFIG['settings']['show_text'] == '0':
    toggle_text_boxes()

win.title("BK Missions Generator")
win.geometry(WIN_SIZE.get())
win.minsize(300, 675)
if CONFIG_ERROR:
    messagebox.showerror('Config Missing!', "Oops! I couldn't find your configuration file (bk_config.ini). Make sure it's in this folder and you didn't change its name. In the meantime, you can continue but you won't be able to change default values.")
logging.info('done with all setup.')
win.mainloop()
