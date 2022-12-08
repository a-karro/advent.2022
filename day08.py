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
        if (
            t > max(row[:x])
            or t > max(row[x+1:])
            or t > max(col[:y])
            or t > max(col[y+1:])
        ):
            visible += 1

        dl = get_score(row[x - 1::-1], t)
        dr = get_score(row[x + 1:], t)
        du = get_score(col[y - 1::-1], t)
        dd = get_score(col[y + 1:], t)

        vd = dl * du * dr * dd
        max_vd = max(vd, max_vd)

print("Puzzle 7.1:", visible)
print("Puzzle 7.2:", max_vd)
