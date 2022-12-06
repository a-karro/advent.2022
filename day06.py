lines = open("data/day06.txt", "r").read()


def start(p_len):
    for i in range(len(lines) - p_len):
        s = set(lines[i: i + p_len])
        if len(s) == p_len:
            return i + p_len


print("Puzzle 6.1:", start(4))
print("Puzzle 6.2:", start(14))
