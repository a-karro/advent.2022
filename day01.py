elves = []

cal = 0

lines = open("data/day01.txt", "r").readlines()
lines.append("\n")

for line in lines:
    if line != "\n":
        cal += int(line)
    else:
        elves.append(cal)
        cal = 0

print("Puzzle 1.1:", max(elves))
print("Puzzle 1.2:", sum(sorted(elves, reverse=True)[:3]))
