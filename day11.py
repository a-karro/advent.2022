from copy import deepcopy


L = open("data/day11.txt", "r").read().split("\n\n")

lcm = 1


class Monkey:
    def __init__(self, desc):
        p = desc.split("\n")
        self.monke = int(p[0].split()[1][:-1])
        self.items = [int(i) for i in p[1].split(":")[1].split(",")]
        self.op = p[2].split("=")[1].strip()
        self.test = int(p[3].split()[-1])
        self.true = int(p[4].split()[-1])
        self.false = int(p[5].split()[-1])
        self.active = 0
        global lcm
        lcm = lcm * self.test

    def do_op(self, x, part2):
        old = x
        a = eval(self.op)
        if part2:
            return a % lcm
        else:
            return a // 3

    def do_business(self, part2):
        throws = []
        self.active += len(self.items)
        for i in self.items:
            wl = self.do_op(i, part2)
            a = wl % self.test
            if a == 0:
                throws.append((wl, self.true))
            else:
                throws.append((wl, self.false))
        self.items = []
        return throws

    def catch_new(self, item):
        self.items.append(item)


M = []
M2 = []
for p in L:
    monke = Monkey(p)
    M.append(monke)

M2 = deepcopy(M)

for i in range(20):
    for m in range(len(M)):
        throws = M[m].do_business(part2=False)
        for k in throws:
            M[k[1]].catch_new(k[0])

for i in range(10000):
    for m in range(len(M2)):
        throws = M2[m].do_business(part2=True)
        for k in throws:
            M2[k[1]].catch_new(k[0])


M = sorted(M, key=lambda x: x.active, reverse=True)
print("Puzzle 11.1:", M[0].active * M[1].active)

M2 = sorted(M2, key=lambda x: x.active, reverse=True)
print("Puzzle 11.3:", M2[0].active * M2[1].active)
