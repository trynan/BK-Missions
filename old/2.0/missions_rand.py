# BK Missions Program
# - Written by Trynan and Wedarobi (but mostly Wedarobi)

from operator import attrgetter
import random

class Mission:
    def __init__(self, cats, types, name: str):
        self.cats = cats
        self.type = types
        self.name = name

if __name__ == "__main__":
    # This code will run when .py is executed directly
    # basically just put code here
    print("BK Missions Program written by trynan_ and Wedarobi.")
    while input("Press enter to generate a new board or press 'q' to quit.\n") != "q":
        # putting missions here so they randomize the random parts every time
        # hopefully it doesn't make it too slow
        # should be fine
        missions = [
        [ # TYPE_MAIN_OBJECTIVE
            Mission(["N"],            "1. Main Objective", "Open 765 Note Door"),
            Mission(["O"],            "1. Main Objective", "All Jinjos"),
            Mission(["N"],            "1. Main Objective", "Defeat Grunty"),
            Mission(["H", "T"],       "1. Main Objective", "All 24 Honeycombs"),
            Mission(["T"],            "1. Main Objective", "All 116 Tokens"),
            Mission(["J"],            "1. Main Objective", "Open All 9 Worlds"),
            Mission(["N", "R"],       "1. Main Objective", "All Notes"),
            Mission(["J", "R"],       "1. Main Objective", "85 Jiggies"),
            Mission(["N", "J", "R"],  "1. Main Objective", "Open DoG and Defeat Grunty"),
            Mission(["J"],            "1. Main Objective", "Humanitarian: Chimpy, Blubber, Raise Clanker/Fix Teeth, Tanktup, Presents, Gobi's Rock, Trunker, Snorkel, Nabnut, Eyrie, Gnawty, Tooty"),
            Mission(["N", "R"],       "1. Main Objective", "Open All 12 Note Doors and Defeat Grunty"),
            Mission(["A"],            "1. Main Objective", "All of 1 Type of Collectible From Each World (All Tokens, HCs, Notes, or Jiggies)"),
        ],
        [ # TYPE_SIDE_QUEST
            Mission(["H", "A"],       "2. Side Quest", "18 HCs"),
            Mission(["T"],            "2. Side Quest", "All 5 Transformations"),
            Mission([],               "2. Side Quest", "All 10 Brentilda Visits"),
            Mission(["O"],            "2. Side Quest", "All 9 Orange Jinjos"),
            Mission(["O"],            "2. Side Quest", "All 9 Blue Jinjos"),
            Mission(["O"],            "2. Side Quest", "All 9 Green Jinjos"),
            Mission(["O"],            "2. Side Quest", "All 9 Pink Jinjos"),
            Mission(["O"],            "2. Side Quest", "All 9 Yellow Jinjos"),
            Mission(["N"],            "2. Side Quest", "Open the 640 Note Door"),
            Mission(["T"],            "2. Side Quest", "90 Tokens"),
            Mission(["J"],            "2. Side Quest", "45 Jiggies"),
            Mission([],               "2. Side Quest", "All 3 Cheato Visits"),
            Mission(["J"],            "2. Side Quest", "2 Jiggies From Each World"),
            Mission(["J"],            "2. Side Quest", "All Lair Jiggies"),
            Mission([],               "2. Side Quest", "Activate All 8 Warp Cauldrons (not dingpot)"),
            Mission(["R"],            "2. Side Quest", "No RBA"),
            Mission(["R"],            "2. Side Quest", "No FFM"),
            Mission(["R", "J"],       "2. Side Quest", "No MMM Early"),
            Mission(["R", "J"],       "2. Side Quest", "No FP Early"),
        ],
        [ # TYPE_EARLY_GAME
            Mission(["O", "A"],       "3. Early Game", "All Jinjos in CC"),
            Mission(["O", "A"],       "3. Early Game", "All Jinjos in FP"),
            Mission(["J", "A"],       "3. Early Game", "{} Jiggies in TTC".format(random.randint(3,10))),
            Mission(["J", "A"],       "3. Early Game", "{} Jiggies in CC".format(random.randint(3,10))),
            Mission(["N", "A"],       "3. Early Game", "{} Notes in CC".format(random.randint(30,100))),
            Mission(["N", "A"],       "3. Early Game", "{} Notes in FP".format(random.randint(30,100))),
            Mission(["H", "A"],       "3. Early Game", "Both HCs in TTC"),
            Mission(["H", "A"],       "3. Early Game", "Both HCs in CC"),
            Mission(["H", "A"],       "3. Early Game", "Both HCs in FP"),
            Mission(["T", "A"],       "3. Early Game", "All 10 Tokens in TTC"),
            Mission(["J"],            "3. Early Game", "All 4 Jiggies Inside Clanker"),
            Mission(["R"],            "3. Early Game", "Begin Run w/ MM 100% Trotless"),
            Mission(["T", "A"],       "3. Early Game", "All 10 Tokens in FP"),
            Mission(["J"],            "3. Early Game", "Merry Christmas! (Visit Boggy's Igloo With Him in it & Give Him Presents)"),
            Mission(["J", "A"],       "3. Early Game", "{} Jiggies in FP".format(random.randint(3,9))),
            Mission(["J", "R"],       "3. Early Game", "No Jiggies in MM"),
            Mission(["J", "T"],       "3. Early Game", "Termite's Quest: 8 Jiggies, 90 Notes, and 1 HC as the Termite"),
        ],
        [ # TYPE_MID_GAME
            Mission(["O", "A"],       "4. Mid Game", "All Jinjos in MMM"),
            Mission(["O", "A"],       "4. Mid Game", "All Jinjos in GV"),
            Mission(["O", "A"],       "4. Mid Game", "All Jinjos in RBB"),
            Mission(["J", "A"],       "4. Mid Game", "{} Jiggies in MMM".format(random.randint(3,10))),
            Mission(["J", "A"],       "4. Mid Game", "{} Jiggies in RBB".format(random.randint(3,10))),
            Mission(["N", "A"],       "4. Mid Game", "{} Notes in MMM".format(random.randint(30,100))),
            Mission(["N", "A"],       "4. Mid Game", "{} Notes in GV".format(random.randint(30,100))),
            Mission(["N", "A"],       "4. Mid Game", "{} Notes in RBB".format(random.randint(30,100))),
            Mission(["H", "A"],       "4. Mid Game", "Both HCs in MMM"),
            Mission(["H", "A"],       "4. Mid Game", "Both HCs in GV"),
            Mission(["H", "A"],       "4. Mid Game", "Both HCs in RBB"),
            Mission(["T", "A"],       "4. Mid Game", "{} Tokens in MMM".format(random.randint(10,16))),
            Mission(["T", "A"],       "4. Mid Game", "All 10 Tokens in GV"),
            Mission(["T", "A"],       "4. Mid Game", "{} Tokens in RBB".format(random.randint(10,15))),
            Mission([],               "4. Mid Game", "MMM Witch Switch Jiggy"),
            Mission([],               "4. Mid Game", "Kill all 10 Limbos (skeletons) in MMM"),
            Mission([],               "4. Mid Game", "GV Rings Jiggy w/o Flight or Bee"),
            Mission(["J"],            "4. Mid Game", "Abuse Gobi (Beak Bust Gobi at all 5 locations)"),
            Mission(["J", "A"],       "4. Mid Game", "{} Jiggies in GV".format(random.randint(3,9))),
        ],
        [ # TYPE_LATE_GAME
            Mission(["O", "A"],       "5. Late Game", "All Jinjos in CCW"),
            Mission(["O", "A"],       "5. Late Game", "All Jinjos in BGS"),
            Mission(["N", "A"],       "5. Late Game", "{} Notes in BGS".format(random.randint(30,100))),
            Mission(["H", "A"],       "5. Late Game", "Both HCs in BGS"),
            Mission(["H", "A"],       "5. Late Game", "Both HCs in CCW"),
            Mission(["T", "A"],       "5. Late Game", "All 10 Tokens in BGS"),
            Mission(["J"],            "5. Late Game", "Croctuses Jiggy"),
            Mission(["J"],            "5. Late Game", "Tiptup's Jiggy"),
            Mission(["J"],            "5. Late Game", "Both Timed Jiggies in BGS"),
            Mission([],               "5. Late Game", "All Caterpillars"),
            Mission(["J"],            "5. Late Game", "Eyrie's Jiggy"),
            Mission(["J"],            "5. Late Game", "Nabnut Jiggy"),
            Mission([],               "5. Late Game", "Kill all 5 Sir Slushes in Winter"),
            Mission(["J"],            "5. Late Game", "Flower Jiggy"),
            Mission(["N", "A"],       "5. Late Game", "{} Notes in CCW".format(random.randint(30,80))),
            Mission(["J", "A"],       "5. Late Game", "{} Jiggies in CCW".format(random.randint(3,8))),
            Mission(["J"],            "5. Late Game", "{} Jiggies in BGS".format(random.randint(3,9))),
            Mission(["T", "A"],       "5. Late Game", "{} Tokens in CCW".format(random.randint(15,25))),
            Mission(["J", "T", "R"],  "5. Late Game", "Collect 10 Jiggies as the Bee"),
        ],
    ]

# --------------------------------------------------------------------------------------------------

        # The Mission instance of each goal as we choose it, in the array 'missions'
        # e.g. [Mission, Mission, Mission]
        goals = []
        # Each category as we come across it, we check against categories in this to make sure we dont repeat them
        # e.g. cats  = ["N", "T", "J"]
        cats1  = []
        cats2 = []
        cats3 = []
        # keep random nums in this list so they're not repeated
        i_list = []
        # numTypes = 7 # tbh i don't know what this variable is for

        for i in range(len(missions)):
            # if len(goals) >= numTypes: break # idk what this does, doesn't seem to break if i take it out
            if i != 0:
                # do the rest (2-5) in a random order
                rand_i = random.randint(1,len(missions)-1)
                while rand_i in i_list:
                    rand_i = random.randint(1,len(missions)-1)
                i_list.append(rand_i)
                count = len(missions[rand_i])
                done = False
                while not done:
                    rn = random.randint(0, count - 1)
                    mission = missions[rand_i][rn]
                    exists = False
                    # if mission in goals: break
                    for c in mission.cats:
                        if c in cats1 or c in cats3:
                            # if category is in the first one or has already happened twice find another mission
                            exists = True
                            break
                    if exists: continue
                    done = True
                
                for c in mission.cats:
                    # if it's already in cats2 then it's happened twice, put it in cats3
                    if c in cats2:
                        cats3.append(c)
                    else:
                        cats2.append(c)

            elif i == 0:
                # do the first goal separate from the rest
                count = len(missions[i])
                rn = random.randint(0, count - 1)
                mission = missions[i][rn]
                for c in mission.cats:
                    cats1.append(c)

            goals.append(mission)

        print("Printing objectives...!\n")
        goals_s = sorted(goals, key=attrgetter('type'))
        for i, e in enumerate(goals_s):
            print(e.type, ": ", e.name, " -- ", ', '.join(e.cats), sep='')
            # print(e.type, ": ", e.name, sep='')
        print("\n-------------------------------------------------------\n")