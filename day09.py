from collections import defaultdict

lines = open("data/day09.txt", "r").read().splitlines()

dirs = [a.split() for a in lines]


def sign(a):
    return (a > 0) - (a < 0)


def solve(length):
    knots = [(0, 0)] * length
    visited = defaultdict(lambda: 0)
    for d in dirs:
        for s in range(int(d[1])):
            hp = knots[0]
            if d[0] == "R":
                hp = (hp[0] + 1, hp[1])
            if d[0] == "L":
                hp = (hp[0] - 1, hp[1])
            if d[0] == "U":
                hp = (hp[0], hp[1] - 1)
            if d[0] == "D":
                hp = (hp[0], hp[1] + 1)
            knots[0] = hp
            prev_moved = True
            for i in range(length - 1):
                if not prev_moved:
                    break
                prev_moved = False
                hp = knots[i]
                tp = knots[i + 1]
                if abs(hp[0] - tp[0]) == 2:
                    if abs(tp[1] - hp[1]) != 0:
                        tp = (tp[0] + sign(hp[0] - tp[0]), tp[1] + sign(hp[1] - tp[1]))
                    else:
                        tp = (tp[0] + sign(hp[0] - tp[0]), tp[1])
                    prev_moved = True

                if abs(hp[1] - tp[1]) == 2:
                    if abs(tp[0] - hp[0]) != 0:
                        tp = (tp[0] + sign(hp[0] - tp[0]), tp[1] + sign(hp[1] - tp[1]))
                    else:
                        tp = (tp[0], tp[1] + sign(hp[1] - tp[1]))
                    prev_moved = True
                knots[i + 1] = tp
            visited[knots[-1]] += 1
    return len(visited)


print("Puzzle 9.1:", solve(2))
print("Puzzle 9.2:", solve(10))
