# BK Missions (short)
# Original written by Trynan and Wedarobi
# Short version adapted by Trynan
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
            Mission(["H"],            "1. Main Objective", "18 HCs"),
            Mission(["T"],            "1. Main Objective", "All 5 Tranformations"),
            Mission(["O"],            "1. Main Objective", "All Jinjos of Any 1 Color (Your Choice)"),
            Mission([],               "1. Main Objective", "All 10 Brentilda Visits"),
            Mission(["N"],            "1. Main Objective", "Open the 640 Note Door"),
            Mission(["T"],            "1. Main Objective", "90 Tokens"),
            Mission(["J"],            "1. Main Objective", "45 Jiggies"),
            Mission([],               "1. Main Objective", "All 3 Cheato Visits"),
            Mission([],               "1. Main Objective", "Activate All 8 Warp Cauldrons (Not Dingpot)"),
            Mission(["T"],            "1. Main Objective", "Save Tooty"),
            Mission(["J"],            "1. Main Objective", "2 Jiggies from each World"),
            Mission(["J"],            "1. Main Objective", "All Lair Jiggies"),
        ],

        [ # TYPE_EARLY_GAME
            Mission(["O", "A"],       "2. Early Game", "All Jinjos in CC"),
            Mission(["O", "A"],       "2. Early Game", "All Jinjos in FP"),
            Mission(["J", "A"],       "2. Early Game", "All Jiggies in TTC"),
            Mission(["J", "A"],       "2. Early Game", "All Jiggies in CC"),
            Mission(["N", "A"],       "2. Early Game", "All Notes in CC"),
            Mission(["N", "A"],       "2. Early Game", "All Notes in FP"),
            Mission(["H", "A"],       "2. Early Game", "Both HCs in TTC"),
            Mission(["H", "A"],       "2. Early Game", "Both HCs in CC"),
            Mission(["H", "A"],       "2. Early Game", "Both HCs in FP"),
            Mission(["T", "A"],       "2. Early Game", "All Tokens in TTC"),
            Mission(["J"],            "2. Early Game", "All 4 Jiggies Inside Clanker"),
            Mission(["R"],            "2. Early Game", "Begin run w/ MM 100% Trotless"),
            Mission(["T", "A"],       "2. Early Game", "All Tokens in FP"),
            Mission(["J"],            "2. Early Game", "Merry Christmas! (Visit Boggy's Igloo w/ Him in it & Give Presents)"),
            Mission(["J", "A"],       "2. Early Game", "9 Jiggies in FP"),
            Mission(["J", "R"],       "2. Early Game", "No Jiggies in MM"),
            Mission(["J", "R"],       "2. Early Game", "Termite's Quest: 8 Jiggies, 90 Notes, & 1 HC as the Termite"),
            Mission(["O", "A"],       "2. Early Game", "All Jinjos in MMM"),
            Mission(["J", "A"],       "2. Early Game", "All Jiggies in MMM"),
            Mission(["N", "A"],       "2. Early Game", "All Notes in MMM"),
            Mission(["H", "A"],       "2. Early Game", "Both HCs in MMM"),
            Mission(["T", "A"],       "2. Early Game", "All Tokens in MMM"),
            Mission([],               "2. Early Game", "MMM Witch Switch Jiggy"),
            Mission([],               "2. Early Game", "Kill all 10 Limbos (skeletons) in MMM"),
        ],

        [ # TYPE_LATE_GAME
            Mission(["O", "A"],       "3. Late Game", "All Jinjos in GV"),
            Mission(["N", "A"],       "3. Late Game", "All Notes in GV"),
            Mission(["H", "A"],       "3. Late Game", "Both HCs in GV"),
            Mission(["T", "A"],       "3. Late Game", "All Tokens in GV"),
            Mission([],               "3. Late Game", "GV Rings Jiggy w/o Flight or Bee"),
            Mission(["J", "A"],       "3. Late Game", "9 Jiggies in GV"),
            Mission(["J"],            "3. Late Game", "Abuse Gobi (Beak Bust Gobi at all 5 locations)"),
            Mission(["O", "A"],       "3. Late Game", "All Jinjos in RBB"),
            Mission(["J", "A"],       "3. Late Game", "All Jiggies in RBB"),
            Mission(["N", "A"],       "3. Late Game", "All Notes in RBB"),
            Mission(["H", "A"],       "3. Late Game", "Both HCs in RBB"),
            Mission(["T", "A"],       "3. Late Game", "All Tokens in RBB"),
            Mission(["O", "A"],       "3. Late Game", "All Jinjos in CCW"),
            Mission(["O", "A"],       "3. Late Game", "All Jinjos in BGS"),
            Mission(["N", "A"],       "3. Late Game", "All Notes in BGS"),
            Mission(["H", "A"],       "3. Late Game", "Both HCs in BGS"),
            Mission(["H", "A"],       "3. Late Game", "Both HCs in CCW"),
            Mission(["T", "A"],       "3. Late Game", "All Tokens in BGS"),
            Mission(["J"],            "3. Late Game", "Croctuses Jiggy"),
            Mission(["J"],            "3. Late Game", "Tiptup's Jiggy"),
            Mission(["J"],            "3. Late Game", "Both Timed Jiggies in BGS"),
            Mission([],               "3. Late Game", "All Caterpillars"),
            Mission(["J"],            "3. Late Game", "Eyrie's Jiggy"),
            Mission(["J"],            "3. Late Game", "Nabnut Jiggy"),
            Mission([],               "3. Late Game", "Kill all 5 Sir Slushes in Winter"),
            Mission(["J"],            "3. Late Game", "Flower Jiggy"),
            Mission(["N", "A"],       "3. Late Game", "80 Notes in CCW"),
            Mission(["J", "A"],       "3. Late Game", "8 Jiggies in CCW"),
            Mission(["J"],            "3. Late Game", "9 Jiggies in BGS"),
            Mission(["T", "A"],       "3. Late Game", "20 Tokens in CCW"),
            Mission(["J", "T", "R"],  "3. Late Game", "Collect 10 Jiggies as the Bee"),
        ],
    ]


# --------------------------------------------------------------------------------------------------

        # The Mission instance of each goal as we choose it, in the array 'missions'
        # e.g. [Mission, Mission, Mission]
        goals = []
        # Each category as we come across it, we check against categories in this to make sure we dont repeat them
        # e.g. cats  = ["N", "T", "J"]
        cats1  = []
        # keep random nums in this list so they're not repeated
        i_list = []
        # numTypes = 7 # tbh i don't know what this variable is for

        for i in range(len(missions)):
            # if len(goals) >= numTypes: break # idk what this does, doesn't seem to break if i take it out
            if i != 0:
                # do the rest (2-3) in a random order
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
                        if c in cats1:
                            # if category is in the first one find a new one
                            exists = True
                            break
                    if exists: continue
                    done = True
                for c in mission.cats:
                    cats1.append(c)

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