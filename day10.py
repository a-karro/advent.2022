L = open("data/day10.txt", "r").read().splitlines()


def signal(p, x):
    if p == 20 or (p - 20) % 40 == 0:
        return p * x
    return 0


def draw(p, x, pix):
    if x-1 <= (p-2) % 40 <= x+1:
        pix[(p-2)] = 1


pos = 1
X = 1
S = 0
P = [0] * 40 * 6

for i in L:
    if i == "noop":
        pos += 1
        draw(pos, X, P)
        S += signal(pos, X)
    else:
        pos += 1
        draw(pos, X, P)
        S += signal(pos, X)
        pos += 1
        draw(pos, X, P)
        X += int(i.split()[1])
        S += signal(pos, X)

print("Puzzle 10.1:", S)
px = {0: "  ", 1: "%%"}
crt = []
for i in range(0, len(P) - 1, 40):
    s = "".join(px[P[j]] for j in range(i, i+40))
    crt.append(s)

print("Puzzle 10.2:")
print("\n".join(crt))
