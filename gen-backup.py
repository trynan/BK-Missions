# ----------------- LONG MISSION GENERATION -----------------
        else:
            b4.config(state = NORMAL)
            b5.config(state = NORMAL)
            goals = []
            codes1 = []
            codes2 = []
            codes3 = []
            i_list = []

            for i in range(len(missions)):
                if i == 0:
                    # do main objective before all else
                    count = len(missions[i])
                    done = False
                    while not done:
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[i][rn1])-1)
                        mission = missions[i][rn1][rn2]
                        if rand_var.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        done = True

                    mission.def_num(i)
                    for c in mission.codes:
                        codes1.append(c)

                elif i != 0:
                    # after i = 0 do them randomly
                    rand_i = random.randint(1,len(missions)-1)
                    while rand_i in i_list:
                        rand_i = random.randint(1,len(missions)-1)
                    i_list.append(rand_i)
                    count = len(missions[rand_i])
                    
                    # get random mission
                    done = False
                    while not done:
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[rand_i][rn1])-1)
                        mission = missions[rand_i][rn1][rn2]
                        if rand_var.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        exists = False
                        for c in mission.codes:
                            if c in codes1 or c in codes3:
                                exists = True
                                break
                        if exists: continue
                        done = True
                    # add mission's codes to list of codes
                    mission.def_num(rand_i)
                    for c in mission.codes:
                        if c in codes2:
                            codes3.append(c)
                        else:
                            codes2.append(c)
                goals.append(mission)
            goals_sort = sorted(goals, key=attrgetter('num'))
            # write the goals to the buttons
            for i,g in enumerate(goals_sort):
                if codes_var.get() == 1:
                    btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
                else: 
                    btextlist[i].set(g.name)

# ----------------- LONG MISSION GENERATION -----------------        
        else:
            goals = []
            codes = []
            i_list = []

            for i in range(len(missions)):
                if i == 0:
                    # do main objective before all else
                    count = len(missions[i])
                    done = False
                    while not done:
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[i][rn1])-1)
                        mission = missions[i][rn1][rn2]
                        if rand_var.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        done = True
                    
                    mission.def_num(i)
                    for c in mission.codes:
                        codes.append(c)

                elif i != 0:
                    # after i = 0 do them randomly
                    rand_i = random.randint(1,len(missions)-1)
                    while rand_i in i_list:
                        rand_i = random.randint(1,len(missions)-1)
                    i_list.append(rand_i)
                    count = len(missions[rand_i])

                    # get random mission
                    done = False
                    while not done:
                        rn1 = random.randint(0, count-1)
                        rn2 = random.randint(0, len(missions[rand_i][rn1])-1)
                        mission = missions[rand_i][rn1][rn2]
                        if rand_var.get() == 1: # nonrandoms only
                            if mission.rand == 1: continue
                        else: # exclude nonrandoms
                            if mission.rand == 2: continue
                        exists = False
                        for c in mission.codes:
                            if c in codes:
                                exists = True
                                break
                        if exists: continue
                        done = True
                    mission.def_num(rand_i)
                    # comment this code below to enable repeating codes for early/late game
                    # if it's commented out that means codes can repeat for 2/3 (as long as they don't share 1's goal)
                    # vvvvvvvvvvvvvvvvvvvvvvv
                    for c in mission.codes:
                        codes.append(c)
                    # ^^^^^^^^^^^^^^^^^^^^^^^
                
                goals.append(mission)
            goals_sort = sorted(goals, key=attrgetter('num'))
            # write the goals to the buttons
            for i,g in enumerate(goals_sort):
                if codes_var.get() == 1:
                    btextlist[i].set(g.name + ' -- ' + ', '.join(g.codes))
                else: 
                    btextlist[i].set(g.name)
            b4t.set("-----")
            b5t.set("-----")
            b4.config(state = DISABLED)
            b5.config(state = DISABLED)