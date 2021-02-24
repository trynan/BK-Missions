# BK Missions
# Written by Trynan and Wedarobi
# Maintained by Trynan

from operator import attrgetter
import random

class Mission:
    def __init__(self, codes, num, name):
        self.codes = codes
        self.num = num
        self.name = name
    
if __name__ == "__main__":
    print("BK Missions Program written by trynan_ and Wedarobi")
    while input("Press enter to generate a new board or press 'q' to quit.\n") != 'q':
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

        # ---------------------------------------------------------------------------------------------------------------------

        goals = []
        codes1 = []
        codes2 = []
        codes3 = []
        i_list = []

        for i in range(len(missions)):
            if i != 0:
                # after i = 0 do them randomly
                rand_i = random.randint(1,len(missions)-1)
                while rand_i in i_list:
                    rand_i = random.randint(1,len(missions)-1)
                i_list.append(rand_i)

                count = len(missions[rand_i])
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

                for c in mission.codes:
                    if c in codes2:
                        codes3.append(c)
                    else:
                        codes2.append(c)
            # ---------------------------------------------------
            elif i == 0:
                # do main objective before all else
                count = len(missions[i])
                rn = random.randint(0, count-1)
                mission = missions[i][rn]
                for c in mission.codes:
                    codes1.append(c)
            
            goals.append(mission)
        # -------------------------------------------------------------------------
        print("Printing objectives...\n")
        goals_sort = sorted(goals, key=attrgetter('num'))
        for m in goals_sort:
            print(m.num, ": ", m.name, " -- ", ', '.join(m.codes), sep='')
        print("\n---------------------------------------------------------\n")