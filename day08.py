from functools import reduce
from operator import mul

lines = open("data/day08.txt", "r").read().splitlines()
T = []
for i in lines:
    T.append([j for j in i])

visible = len(T[0]) * 2 + (len(T) - 2) * 2


def get_score(part, _t):
    s = 0
    for n in part:
        s += 1
        if n >= _t:
            break
    return s


max_vd = 0
for y in range(1, len(T) - 1):
    for x in range(1, len(T[0]) - 1):
        row = T[y]
        col = [T[i][x] for i in range(len(T))]
        t = T[y][x]
        l = row[x - 1::-1]
        r = row[x + 1:]
        u = col[y - 1::-1]
        d = col[y + 1:]
        dirs = [l, r, u, d]

        if any(t > max(dr) for dr in dirs):
            visible += 1
        vd = reduce(mul, [get_score(dr, t) for dr in dirs])

        max_vd = max(vd, max_vd)

print("Puzzle 7.1:", visible)
print("Puzzle 7.2:", max_vd)
