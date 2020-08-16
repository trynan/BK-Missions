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

mis = Mission(0, ['k'], '765 note door')

for a in range(100):
    mis.inc_count()
print(mis.count)