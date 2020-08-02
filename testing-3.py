x = [
    [1, 2, 3],
    [4, 5, 6]
]

even = 1

for i in x:
    for a in i:
        if even == 1:
            if a % 2 == 0: continue
        else:
            if a % 2 != 0: continue
        print(a)