lines = open("data/day02.txt", "r").readlines()

values = {"X": 1,
          "Y": 2,
          "Z": 3}

scores = [6, 3, 0]


outcomes = {"A": ["Y", "X", "Z"],
            "B": ["Z", "Y", "X"],
            "C": ["X", "Z", "Y"]}

outcomes2 = {"X": 2,
             "Y": 1,
             "Z": 0}

s1 = s2 = 0
for x in lines:
    elf, you = x.split()
    s1 += values[you] + scores[outcomes[elf].index(you)]
    s2 += scores[outcomes2[you]] + values[outcomes[elf][outcomes2[you]]]

print("Puzzle 2.1:", s1)
print("Puzzle 2.2:", s2)
