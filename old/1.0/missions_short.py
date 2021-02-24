# BK Missions (short)
# Written by Trynan

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
        Mission(["H"],          "18 Honeycombs"),
        Mission(["T"],          "All 5 Transformations"),
        Mission(["N"],          "Open the 450 Note Door"),
        Mission([],             "Talk to All 10 Brentildas"),
        Mission(["N"],          "Open the 640 Note Door"),
        Mission(["T"],          "90 Mumbo Tokens"),
        Mission(["J"],          "45 Jiggies"),
        Mission([],             "All 3 Cheato Visits"),
        Mission([],             "Activate All 8 Warp Cauldrons (not Dingpot)"),
        Mission(["T"],          "Save Tooty"),
    ],

    [ # TYPE_EARLY_GAME
        Mission(["O"],            "All Jinjos in CC"),
        Mission(["J"],            "All Jiggies in CC"),
        Mission(["J"],            "All 4 Jiggies Inside Clanker"),
        Mission(["J"],            "Merry Christmas! (Visit Boggy's Igloo With Him in it & Give Him Presents)"),
        Mission(["H"],            "Both HC's in FP"),
        Mission(["J"],            "All FP Jiggies w/o Using the Flight Pad on the Presents"),
        Mission(["T", "J"],       "All Tokens in FP"),
        Mission([],               "Begin Run w/ MM 100% Trotless"),
        Mission(["R", "J"],       "No Jiggies in MM"),
        Mission(["J"],            "X Marks the Spot Jiggy in TTC"),
        Mission(["N"],            "All Notes in TTC"),
        Mission(["J"],            "Sandcastle Jiggy"),
        Mission([],             "MMM Witch Switch Jiggy as Banjo w/o Flight"),
        Mission(["J"],            "Flower Pots Jiggy w/o Killing Gravestones"),
        Mission(["T"],            "All Tokens in MMM"),
        Mission([],             "Kill All 10 Skeletons in MMM"),

    ],

    [ # TYPE_LATE_GAME
         Mission(["N"],            "All Notes in BGS"),
        Mission(["J"],            "Croctuses' Jiggy"),
        Mission(["J"],            "Tiptup's Jiggy"),
        Mission(["J"],            "Both Timed Jiggies in BGS"),
        Mission(["O"],            "All Jinjos in BGS"),
        Mission([],               "All Caterpillars"),
        Mission(["J"],            "Eyrie's Jiggy"),
        Mission(["J"],            "Nabnut's Jiggy"),
        Mission(["T"],            "All Tokens in CCW"),
        Mission(["H"],            "Both HCs in CCW"),
        Mission([],               "Kill all 5 Sir Slushes in Winter"),
        Mission(["N"],            "All Notes in CCW"),
        Mission(["N"],            "All Notes in GV"),
        Mission(["N"],            "All Notes in GV"),
        Mission([],               "GV Rings Jiggy w/o Flight"),
        Mission(["J"],            "Abuse Gobi (Beak Bust Gobi at All 5 Locations)"),
        Mission(["H"],            "All HC's in GV"),
        Mission([""],             "MMM Witch Switch Jiggy as Banjo w/o Flight"),
        Mission(["J"],            "Flower Pots Jiggy w/o Killing Gravestones"),
        Mission(["T"],            "All Tokens in MMM"),
        Mission([],               "Kill All 10 Skeletons in MMM"),
        Mission(["O"],            "All Jinjos in RBB"),
        Mission(["J"],            "All Jiggies in RBB"),
        Mission(["J"],            "Save Snorkel Jiggy"),
        Mission(["J"],            "Propeller Jiggy in RBB"),
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
        numTypes = 5

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
            if i < 2:
                for c in mission.cats:
                    cats.append(c)
            goals.append(mission)

        print("Printing objectives...!\n")
        for i, e in enumerate(goals):
            # print(e.name, ", cats:", e.cats, ", type:", e.type,sep='')
            print(i+1, ". ", e.name, sep='')
        print("\n-------------------------------------------------------\n")