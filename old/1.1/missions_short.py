# BK Missions (short)
# Original written by Trynan and Wedarobi
# Short version adapted by Trynan

import random

class Mission:
    def __init__(self, cats, name: str):
        self.name = name
        # self.type = mType
        self.cats = cats
        self.type = 0
        
    def set_type(self, mType):
        self.type = mType

# format: Mission(["category"], "goal name"),
# to add a tag onto a level follow the format Mission(["cat1", "cat2"])
missions = [
    [ # TYPE_MAIN_OBJECTIVE
        Mission(["H"],                  "18 HCs"),
        Mission(["T"],                  "All 5 Tranformations"),
        Mission(["O"],                  "All Jinjos of Any 1 Color (Your Choice)"),
        Mission([],                     "All 10 Brentilda Visits"),
        Mission(["N"],                  "Open the 640 Note Door"),
        Mission(["T"],                  "90 Tokens"),
        Mission(["J"],                  "45 Jiggies"),
        Mission([],                     "All 3 Cheato Visits"),
        Mission([],                     "Activate All 8 Warp Cauldrons (Not Dingpot)"),
        Mission(["T"],                  "Save Tooty"),
        Mission(["J"],                  "2 Jiggies from each World"),
        Mission(["J"],                  "All Lair Jiggies"),
    ],

    [ # TYPE_EARLY_GAME
        Mission(["O", "A"],             "All Jinjos in CC"),
        Mission(["O", "A"],             "All Jinjos in FP"),
        Mission(["J", "A"],             "All Jiggies in TTC"),
        Mission(["J", "A"],             "All Jiggies in CC"),
        Mission(["N", "A"],             "All Notes in CC"),
        Mission(["N", "A"],             "All Notes in FP"),
        Mission(["H", "A"],             "Both HCs in TTC"),
        Mission(["H", "A"],             "Both HCs in CC"),
        Mission(["H", "A"],             "Both HCs in FP"),
        Mission(["T", "A"],             "All Tokens in TTC"),
        Mission(["J"],                  "All 4 Jiggies Inside Clanker"),
        Mission(["R"],                  "Begin run w/ MM 100% Trotless"),
        Mission(["T", "A"],             "All Tokens in FP"),
        Mission(["J"],                  "Merry Christmas! (Visit Boggy's Igloo w/ Him in it & Give Presents)"),
        Mission(["J", "A"],             "9 Jiggies in FP"),
        Mission(["J", "R"],             "No Jiggies in MM"),
        Mission(["J", "R"],             "Termite's Quest: 8 Jiggies, 90 Notes, & 1 HC as the Termite"),
        Mission(["O", "A"],             "All Jinjos in MMM"),
        Mission(["J", "A"],             "All Jiggies in MMM"),
        Mission(["N", "A"],             "All Notes in MMM"),
        Mission(["H", "A"],             "Both HCs in MMM"),
        Mission(["T", "A"],             "All Tokens in MMM"),
        Mission([],                     "MMM Witch Switch Jiggy"),
        Mission([],                     "Kill all 10 Limbos (skeletons) in MMM"),
    ],

    [ # TYPE_LATE_GAME
        Mission(["O", "A"],             "All Jinjos in GV"),
        Mission(["N", "A"],             "All Notes in GV"),
        Mission(["H", "A"],             "Both HCs in GV"),
        Mission(["T", "A"],             "All Tokens in GV"),
        Mission([],                     "GV Rings Jiggy w/o Flight or Bee"),
        Mission(["J", "A"],             "9 Jiggies in GV"),
        Mission(["J"],                  "Abuse Gobi (Beak Bust Gobi at all 5 locations)"),
        Mission(["O", "A"],             "All Jinjos in RBB"),
        Mission(["J", "A"],             "All Jiggies in RBB"),
        Mission(["N", "A"],             "All Notes in RBB"),
        Mission(["H", "A"],             "Both HCs in RBB"),
        Mission(["T", "A"],             "All Tokens in RBB"),
        Mission(["O", "A"],             "All Jinjos in CCW"),
        Mission(["O", "A"],             "All Jinjos in BGS"),
        Mission(["N", "A"],             "All Notes in BGS"),
        Mission(["H", "A"],             "Both HCs in BGS"),
        Mission(["H", "A"],             "Both HCs in CCW"),
        Mission(["T", "A"],             "All Tokens in BGS"),
        Mission(["J"],                  "Croctuses Jiggy"),
        Mission(["J"],                  "Tiptup's Jiggy"),
        Mission(["J"],                  "Both Timed Jiggies in BGS"),
        Mission([],                     "All Caterpillars"),
        Mission(["J"],                  "Eyrie's Jiggy"),
        Mission(["J"],                  "Nabnut Jiggy"),
        Mission([],                     "Kill all 5 Sir Slushes in Winter"),
        Mission(["J"],                  "Flower Jiggy"),
        Mission(["N", "A"],             "80 Notes in CCW"),
        Mission(["J", "A"],             "8 Jiggies in CCW"),
        Mission(["J"],                  "9 Jiggies in BGS"),
        Mission(["T", "A"],             "20 Tokens in CCW"),
        Mission(["J", "T", "R"],        "Collect 10 Jiggies as the Bee"),
    ],
]

if __name__ == "__main__":
    # This code will run when .py is executed directly
    # basically just put code here
    print("BK Missions Program written by trynan_ and Wedarobi.")
    while input("Press enter to generate a new board or press 'q' to quit.\n") != "q":
        # The Mission instance of each goal as we choose it, in the array `missions`
        # e.g. [Mission, Mission, Mission]
        goals = []
        # Each category as we come across it, we check against categories in this to make sure we dont repeat them
        # e.g. cats  = ["N", "T", "J"]
        cats  = []
        numTypes = 7

        for i in range(len(missions)):
            if len(goals) >= numTypes: break
            count = len(missions[i])
            done = False
            while not done:
                rn = random.randint(0, count - 1)
                mission = missions[i][rn]
                exists = False
                # if mission in goals: break
                for c in mission.cats:
                    if c in cats:
                        exists = True
                        break
                if exists: continue
                done = True

            mission.set_type(i)
            # if i < 2:
            for c in mission.cats:
                cats.append(c)
            goals.append(mission)

        print("Printing objectives...!\n")
        for i, e in enumerate(goals):
            # print(e.name, ", cats:", e.cats, ", type:", e.type,sep='')
            print(i+1, ". ", e.name, sep='')
        print("\n-------------------------------------------------------\n")