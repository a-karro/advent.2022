from collections import defaultdict
from copy import deepcopy

C, I = map(lambda a: a.split("\n"), open("data/day05.txt", "r").read().split("\n\n"))

s = defaultdict(list)

total = (len(C[-1]) - 2) // 4 + 1
idx = [1] + [(i + 1) * 4 + 1 for i in range(total - 1)]

for c in C[:-1][::-1]:
    for i, n in enumerate(idx):
        if len(c) > n and c[n] != " ":
            s[i + 1].append(c[n])

s2 = deepcopy(s)

for i in I:
    amt, src, dst = [*map(int, i.split(" ")[1::2])]
    for c in range(amt):
        s[dst].append(s[src].pop())
    s2[dst].extend(s2[src][-amt:])
    s2[src] = s2[src][:-amt]

print("Puzzle 5.1:", "".join(s[i].pop() for i in s if len(s[i]) > 0))
print("Puzzle 5.2:", "".join(s2[i].pop() for i in s2 if len(s2[i]) > 0))
