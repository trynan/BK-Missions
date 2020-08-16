# testing
# https://www.tutorialspoint.com/python3/python_gui_programming.htm

from operator import attrgetter
import random

class Mission:
    def __init__(self, rand, codes, name):
        self.rand = rand
        self.codes = codes
        self.name = name
    count = 0

    def def_num(self, num):
        self.num = num
    
    def inc_count(self):
        self.count += 1

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
shortvar = int(input("0 for long, 1 for short"))

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
    Mission(0, ["J"],           "Humanitarian"),
    Mission(0, ["N", "R"],      "Open All 12 Note Doors and Defeat Grunty"),
    Mission(0, ["A"],           "All of 1 type of collectible from each world"),
]
long_side = [
    Mission(1, ["H", "A"],      "{} HCs [r 14-18]".format(random.randint(14,18))),
    Mission(2, ["H", "A"],      "18 HCs"),
    Mission(0, ["T"],           "All 5 transformations"),
    Mission(0, [],              "All 10 Brentilda visits"),
    Mission(0, ["O"],           "All 9 orange Jinjos"),
    Mission(0, ["O"],           "All 9 blue Jinjos"),
    Mission(0, ["O"],           "All 9 green Jinjos"),
    Mission(0, ["O"],           "All 9 pink Jinjos"),
    Mission(0, ["O"],           "All 9 yellow Jinjos"),
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

x = int(input("how many runs?"))
input("enter to start\n")
for blah in range(x):
    if not shortvar: # long missions
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

        # ----------------- LONG MISSION GENERATION -----------------
        goals = []
        codes1 = []
        codes2 = []
        codes3 = []
        i_list =[]

        for i in range(len(missions)):
            if i == 0:
                # do main objective first
                count = len(missions[i])
                done = False
                while not done:
                    rn1 = random.randint(0, count-1)
                    rn2 = random.randint(0, len(missions[i][rn1])-1)
                    mission = missions[i][rn1][rn2]
                    if mission.rand == 2: continue
                    done = True
                
                mission.def_num(i)
                for c in mission.codes:
                    codes1.append(c)
            
            elif i != 0:
                rand_i = random.randint(1, len(missions)-1)
                while rand_i in i_list:
                    rand_i = random.randint(1,len(missions)-1)
                i_list.append(rand_i)
                count = len(missions[rand_i])

                done = False
                while not done:
                    rn1 = random.randint(0, count-1)
                    rn2 = random.randint(0, len(missions[rand_i][rn1])-1)
                    mission = missions[rand_i][rn1][rn2]
                    if mission.rand == 2: continue
                    exists = False
                    for c in mission.codes:
                        if c in codes1 or c in codes3:
                            exists = True
                            break
                    if exists: continue
                    done = True

                mission.def_num(rand_i)
                for c in mission.codes:
                    if c in codes2:
                        codes3.append(c)
                    else:
                        codes2.append(c)
            goals.append(mission)

        for goal in goals:
            goal.inc_count()
        


    elif shortvar: # short missions
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

        # ----------------- SHORT MISSION GENERATION -----------------
        goals = []
        codes = []
        i_list = []

        for i in range(len(missions)):
            if i == 0:
                # do main objectives before the rest
                count = len(missions[i])
                done = False
                while not done:
                    rn1 = random.randint(0, count-1)
                    rn2 = random.randint(0, len(missions[i][rn1])-1)
                    mission = missions[i][rn1][rn2]
                    if mission.rand ==2: continue
                    done = True

                mission.def_num(i)
                for c in mission.codes:
                    codes.append(c)
            
            elif i != 0:
                rand_i = random.randint(1, len(missions)-1)
                while rand_i in i_list:
                    rand_i = random.randint(1,len(missions)-1)
                i_list.append(rand_i)
                count = len(missions[rand_i])

                done = False
                while not done:
                    rn1 = random.randint(0, count-1)
                    rn2 = random.randint(0, len(missions[rand_i][rn1])-1)
                    mission = missions[rand_i][rn1][rn2]
                    if mission.rand == 2: continue
                    exists = False
                    for c in mission.codes:
                        if c in codes:
                            exists = True
                            break
                    if exists: continue
                    done = True

                mission.def_num(rand_i)
                for c in mission.codes:
                    codes.append(c)
            goals.append(mission)
        
        for goal in goals:
            goal.inc_count()

finalstring = ''
with open('data.csv', 'w') as data:
    for i,label in enumerate(missions):
        if shortvar == 0:
            finalstring += long_label_list[i] + '\n'
        elif shortvar == 1:
            finalstring += short_label_list[i] + '\n'
        for category in label:
            for gol in category:
                if gol.rand == 2: continue
                finalstring += gol.name + ',' + str(gol.count) + ','
                for c in gol.codes:
                    finalstring += c
                finalstring += '\n'
                # print(type(gol.name), type(gol.count))
        finalstring += '\n'
    data.write(finalstring)