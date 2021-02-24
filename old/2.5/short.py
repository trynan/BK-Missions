# BK Missions (short)
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

        # ---------------------------------------------------------------------------------------------------------------------

        goals = []
        codes = []
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
            # ---------------------------------------------------
            elif i == 0:
                # do main objective before all else
                count = len(missions[i])
                rn = random.randint(0, count-1)
                mission = missions[i][rn]
                for c in mission.codes:
                    codes.append(c)
            
            goals.append(mission)
        # -------------------------------------------------------------------------
        print("Printing objectives...\n")
        goals_sort = sorted(goals, key=attrgetter('num'))
        for m in goals_sort:
            print(m.num, ": ", m.name, " -- ", ', '.join(m.codes), sep='')
        print("\n---------------------------------------------------------\n")