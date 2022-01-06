# file for storing missions and the mission generation functions.

import random
from operator import attrgetter

class Mission:
    def __init__(self, rand, codes, name):
        self.rand = rand  # int, 0 means normal, 1 means random, 2 means normal variant of a random goal
        self.codes = codes  # list of codes, i.e. ["N", "A"]
        self.name = name  # name of goal (string), i.e. "Open 765 note door"


def getRandI(length, i_list):
    """
    Gets a random i based on length which isn't in i_list.
    - length is an integer for how many i's there will be.
    - i_list is a list of previous i's that have been used already.

    - return: int which is not found in i_list.
    """
    rand_i = random.randrange(1, length)
    while rand_i in i_list:
        rand_i = random.randrange(1, length)
    # i_list gets appended to in place, it carries over
    i_list.append(rand_i)
    return rand_i


def randomMission(missionsList, codes, randomize):
    """
    Gets a random mission from missionsList while excluding codes in the codes list.
    - missionsList is a list of lists of missions.
    - codes is a list of codes.
    - randomize is a bool for whether the goals themselves 
      have random amounds in them (true --> don't randomize).

    - return: Mission object.
    """
    count = len(missionsList)
    done = False
    while not done:
        rn1 = random.randrange(0, count)
        rn2 = random.randrange(0, len(missionsList[rn1]))
        mission = missionsList[rn1][rn2]
        if randomize:  # exclude randoms
            if mission.rand == 1:
                continue
        else:  # exclude nonrandoms
            if mission.rand == 2:
                continue
        # search for conflicting codes
        exists = False
        for c in mission.codes:
            if c in codes:
                exists = True
                break
        if exists:
            continue
        done = True
    return mission


def generateGoals(missions, short, randomize):
    """
    Generates a set of five or three (depending on long/short) missions.
    - missions is a list of lists of lists of mission objects.
    - short is a bool (true --> short missions will be generated).
    Logic (long):
    - randomize is a bool for whether goal amounts should be randomized (true --> don't randomize).
    ---
    - Choose the first (main) goal randomly.
    - Put that goal's codes in the codes1 list.
    - Choose the next category of goals randomly.
    - Choose the goal from that category randomly, making sure it has
      no conflicts with the codes in the codes3 list.
    - Put that goal's codes in the codes1 list.
    - If there are any repeated goals in codes1, move it to codes2.
    - If there are any repeated goals in codes2, move it to codes3.
    - Repeat until five goals have been generated.

    Logic (short):
    ---
    - Same as long with some minor differences.
    - The first mission's codes are immediately added to codes3
      to be excluded in the other two missions.
    - Otherwise, the other missions do not add their codes to any
      codes lists.

    This function sorts the chosen goals and returns them.
    """
    goals = []
    codes1 = []
    codes2 = []  # intermediary
    codes3 = []  # if codes are present twice, then remove them
    i_list = []

    for i in range(len(missions)):
        if not i:
            rand_i = 0
            mission = randomMission(missions[i], codes3, randomize)
        else:
            # after i = 0 do them randomly
            rand_i = getRandI(len(missions), i_list)
            mission = randomMission(missions[rand_i], codes3, randomize)

        mission.num = rand_i
        if short and not i:  # exclude codes from short main category, but no other short categories
            for c in mission.codes:
                codes3.append(c)
        elif not short:
            for c in mission.codes:
                if c in codes2:
                    codes3.append(c)
                elif c in codes1:
                    codes2.append(c)
                else:
                    codes1.append(c)
        goals.append(mission)
    sortedGoals = sorted(goals, key=attrgetter('num'))
    return sortedGoals


def getLongMain():
    """
    Returns the list of mission objects for the long main category.
    """
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


def getLongSide():
    """
    Returns the list of mission objects for the long side category.
    """
    jinjo_list = [
    "purple",
    "green",
    "blue",
    "yellow",
    "orange"
    ]
    return [
        Mission(1, ["H", "A"],      f"{random.randint(14,18)} HCs [r 14-18]"),
        Mission(2, ["H", "A"],      "18 HCs"),
        Mission(0, ["T"],           "All 5 transformations"),
        Mission(0, [],              "All 10 Brentilda visits"),
        Mission(0, ["O"],           f"All 9 {random.choice(jinjo_list)} Jinjos (color randomly chosen)"),
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


def getShortMain():
    """
    Returns the list of mission objects for the short main category.
    """
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


def getLevels():
    """
    Returns a dictionary where keys are levels and values are
    lists of mission objects for the respective level category.
    """
    return {
        'mm': [
            Mission(0, ["R"],           "Begin run w/ MM 100% Trotless"),
            Mission(0, ["J", "R"],      "No more than 2 jiggies in MM"),
            Mission(0, [],              "Termite's Quest: 5 jiggies and 1 HC as the termite"),
        ],
        'ttc': [
            Mission(1, ["J", "A"],      f"{random.randint(8,10)} jiggies in TTC [r 8-10]"),
            Mission(2, ["J", "A"],      "All jiggies in TTC"),
            Mission(0, ["H", "A"],      "Both HCs in TTC"),
            Mission(0, ["T", "A"],      "All tokens in TTC"),
        ],
        'cc': [
            Mission(0, ["O", "A"],      "All Jinjos in CC"),
            Mission(1, ["J", "A"],      f"{random.randint(8,10)} jiggies in CC [r 8-10]"),
            Mission(2, ["J", "A"],      "All jiggies in CC"),
            Mission(1, ["N", "A"],      f"{random.randint(80,100)} notes in CC [r 80-100]"),
            Mission(2, ["N", "A"],      "All notes in CC"),
            Mission(0, ["H", "A"],      "Both HCs in CC"),
            Mission(0, ["J"],           "All 4 jiggies inside Clanker"),
        ],
        'fp': [
            Mission(0, ["O", "A"],      "All Jinjos in FP"),
            Mission(1, ["N", "A"],      f"{random.randint(80,100)} notes in FP [r 80-100]"),
            Mission(2, ["N", "A"],      "All notes in FP"),
            Mission(0, ["H", "A"],      "Both HCs in FP"),
            Mission(0, ["T", "A"],      "All tokens in FP"),
            Mission(0, ["J"],           "Merry Christmas! (Visit Boggy's igloo w/ him in it & give presents)"),
            Mission(1, ["J", "A"],      f"{random.randint(4,9)} jiggies in FP [r 4-9]"),
            Mission(2, ["J", "A"],      "9 jiggies in FP"),
        ],
        'mmm': [
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
        'gv': [
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
        'rbb': [
            Mission(0, ["O", "A"],      "All Jinjos in RBB"),
            Mission(1, ["J", "A"],      f"{random.randint(4,10)} jiggies in RBB [r 4-10]"),
            Mission(2, ["J", "A"],      "All jiggies in RBB"),
            Mission(1, ["N", "A"],      f"{random.randint(40,100)} notes in RBB [r 40-100]"),
            Mission(2, ["N", "A"],      "All notes in RBB"),
            Mission(0, ["H", "A"],      "Both HCs in RBB"),
            Mission(1, ["T", "A"],      f"{random.randint(10,15)} tokens in RBB [r 10-15]"),
            Mission(2, ["T", "A"],      "All tokens in RBB"),
        ],
        'ccw': [
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
        'bgs': [
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
