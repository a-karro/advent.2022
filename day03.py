import string

L = [a for a in open("data/day03.txt", "r").read().split("\n") if a]
P = string.ascii_lowercase + string.ascii_uppercase

p1 = []
for a in L:
    b = len(a) // 2
    p1.extend(c for c in set(a[:b]) if c in set(a[b:]))
print("Puzzle 3.1:", sum(P.index(a) + 1 for a in p1))

p2 = []
for i in range(0, len(L), 3):
    p2.extend(c for c in set(L[i]) if c in set(L[i + 1]) and c in set(L[i + 2]))
print("Puzzle 3.2:", sum(P.index(a) + 1 for a in p2))
