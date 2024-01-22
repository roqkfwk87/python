# 2x1=2 3x1=3 4x1=4 ... 9x1=9
# 2x2=4 3x2=6 4x2=8 ... 9x2=18
# .

n = 1
while n <= 9:
    dan = 2
    while dan <= 9:
        print(f"{dan}×{n}={dan*n}", end="\t")
        dan += 1
    n += 1
    print()