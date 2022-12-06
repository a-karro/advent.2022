P = open("data/day04.txt", "r").read().splitlines()

p1 = p2 = 0
for p in P:
    p = p.replace("-", ",").replace(" ", "")
    r = [*map(int, p.split(","))]
    r1 = [i for i in range(r[0], r[1] + 1)]
    r2 = [i for i in range(r[2], r[3] + 1)]
    if all(i in r1 for i in r2) or all(i in r2 for i in r1):
        p1 += 1
    if any(i in r1 for i in r2) or any(i in r2 for i in r1):
        p2 += 1
print("Puzzle 4.1:", p1)
print("Puzzle 4.2:", p2)
