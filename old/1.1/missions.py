# BK Missions Program
# - Written by Trynan and Wedarobi (but mostly Wedarobi)


import random

class Mission:
    def __init__(self, cats, name: str):
        self.name = name
        # self.type = mType
        self.cats = cats
        self.type = 0
        
    def set_type(self, mType):
        self.type = mType

missions = [
    [ # TYPE_MAIN_OBJECTIVE
        Mission(["N"],            "Open 765 Note Door"),
        Mission(["O"],            "All Jinjos"),
        Mission(["N"],            "Defeat Grunty"),
        Mission(["H", "T"],       "All 24 Honeycombs"),
        Mission(["T"],            "All 116 Tokens"),
        Mission(["J"],            "Open All 9 Worlds"),
        Mission(["N", "R"],       "All Notes"),
        Mission(["J", "R"],       "85 Jiggies"),
        Mission(["N", "J", "R"],  "Open DoG and Defeat Grunty"),
        Mission(["J"],            "Humanitarian: Chimpy, Blubber, Raise Clanker/Fix Teeth, Tanktup, Presents, Gobi's Rock, Trunker, Snorkel, Nabnut, Eyrie, Gnawty, Tooty"),
        Mission(["N", "R"],       "Open All 12 Note Doors and Defeat Grunty"),
        Mission(["A"],            "All of 1 Type of Collectible From Each World (All Tokens, HCs, Notes, or Jiggies)"),
    ],
    [ # TYPE_SIDE_QUEST
        Mission(["H", "A"],       "18 HCs"),
        Mission(["T"],            "All 5 Transformations"),
        Mission([],               "All 10 Brentilda Visits"),
        Mission(["O"],            "All 9 Orange Jinjos"),
        Mission(["O"],            "All 9 Blue Jinjos"),
        Mission(["O"],            "All 9 Green Jinjos"),
        Mission(["O"],            "All 9 Pink Jinjos"),
        Mission(["O"],            "All 9 Yellow Jinjos"),
        Mission(["N"],            "Open the 640 Note Door"),
        Mission(["T"],            "90 Tokens"),
        Mission(["J"],            "45 Jiggies"),
        Mission([],               "All 3 Cheato Visits"),
        Mission(["J"],            "2 Jiggies From Each World"),
        Mission(["J"],            "All Lair Jiggies"),
        Mission([],               "Activate All 8 Warp Cauldrons (not dingpot)"),
        Mission(["R"],            "No RBA"),
        Mission(["R"],            "No FFM"),
        Mission(["R", "J"],       "No MMM Early"),
        Mission(["R", "J"],       "No FP Early"),
    ],
    [ # TYPE_EARLY_GAME
        Mission(["O", "A"],       "All Jinjos in CC"),
        Mission(["O", "A"],       "All Jinjos in FP"),
        Mission(["J", "A"],       "All Jiggies in TTC"),
        Mission(["J", "A"],       "All Jiggies in CC"),
        Mission(["N", "A"],       "All Notes in CC"),
        Mission(["N", "A"],       "All Notes in FP"),
        Mission(["H", "A"],       "Both HCs in TTC"),
        Mission(["H", "A"],       "Both HCs in CC"),
        Mission(["H", "A"],       "Both HCs in FP"),
        Mission(["T", "A"],       "All Tokens in TTC"),
        Mission(["J"],            "All 4 Jiggies Inside Clanker"),
        Mission(["R"],            "Begin Run w/ MM 100% Trotless"),
        Mission(["T", "A"],       "All Tokens in FP"),
        Mission(["J"],            "Merry Christmas! (Visit Boggy's Igloo With Him in it & Give Him Presents)"),
        Mission(["J", "A"],       "9 Jiggies in FP"),
        Mission(["J", "R"],       "No Jiggies in MM"),
        Mission(["J", "T"],       "Termite's Quest: 8 Jiggies, 90 Notes, and 1 HC as the Termite"),
    ],
    [ # TYPE_MID_GAME
        Mission(["O", "A"],       "All Jinjos in MMM"),
        Mission(["O", "A"],       "All Jinjos in GV"),
        Mission(["O", "A"],       "All Jinjos in RBB"),
        Mission(["J", "A"],       "All Jiggies in MMM"),
        Mission(["J", "A"],       "All Jiggies in RBB"),
        Mission(["N", "A"],       "All Notes in MMM"),
        Mission(["N", "A"],       "All Notes in GV"),
        Mission(["N", "A"],       "All Notes in RBB"),
        Mission(["H", "A"],       "Both HCs in MMM"),
        Mission(["H", "A"],       "Both HCs in GV"),
        Mission(["H", "A"],       "Both HCs in RBB"),
        Mission(["T", "A"],       "All Tokens in MMM"),
        Mission(["T", "A"],       "All Tokens in GV"),
        Mission(["T", "A"],       "All Tokens in RBB"),
        Mission([],               "MMM Witch Switch Jiggy"),
        Mission([],               "Kill all 10 Limbos (skeletons) in MMM"),
        Mission([],               "GV Rings Jiggy w/o Flight/Bee"),
        Mission(["J"],            "Abuse Gobi (Beak Bust Gobi at all 5 locations)"),
        Mission(["J", "A"],       "9 Jiggies in GV"),
    ],
    [ # TYPE_LATE_GAME
        Mission(["O", "A"],       "All Jinjos in CCW"),
        Mission(["O", "A"],       "All Jinjos in BGS"),
        Mission(["N", "A"],       "All Notes in BGS"),
        Mission(["H", "A"],       "Both HCs in BGS"),
        Mission(["H", "A"],       "Both HCs in CCW"),
        Mission(["T", "A"],       "All Tokens in BGS"),
        Mission(["J"],            "Croctuses Jiggy"),
        Mission(["J"],            "Tiptup's Jiggy"),
        Mission(["J"],            "Both Timed Jiggies in BGS"),
        Mission([],               "All Caterpillars"),
        Mission(["J"],            "Eyrie's Jiggy"),
        Mission(["J"],            "Nabnut Jiggy"),
        Mission([],               "Kill all 5 Sir Slushes in Winter"),
        Mission(["J"],            "Flower Jiggy"),
        Mission(["N", "A"],       "80 Notes in CCW"),
        Mission(["J", "A"],       "8 Jiggies in CCW"),
        Mission(["J"],            "9 Jiggies in BGS"),
        Mission(["T", "A"],       "20 Tokens in CCW"),
        Mission(["J", "T", "R"],  "Collect 10 Jiggies as the Bee"),
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
            if i < 2:
                for c in mission.cats:
                    cats.append(c)
            goals.append(mission)

        print("Printing objectives...!\n")
        for i, e in enumerate(goals):
            # print(e.name, ", cats:", e.cats, ", type:", e.type,sep='')
            print(i+1, ". ", e.name, sep='')
        print("\n-------------------------------------------------------\n")