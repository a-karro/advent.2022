lines = open("data/day07.txt", "r").read().splitlines()


class Dir:
    def __init__(self, parent, name, dirs):
        self.name = name
        self.parent = parent
        self.dirs = dirs
        self.dirsize = 0


root = Dir(None, "/", [])
current = root

pos = 1

dirs = [root]

while pos < len(lines):
    line = lines[pos].strip()
    if line == "":
        break
    p = line.split()
    if p[0] == "$":
        if p[1] == "cd":
            if p[2] == "/":
                current = root
            elif p[2] == "..":
                current = current.parent
            else:
                idx = next(i for i, n in enumerate(current.dirs) if n.name == p[2])
                current = current.dirs[idx]
            pos += 1
        if p[1] == "ls":
            pos += 1
            while pos < len(lines) and not lines[pos].startswith("$"):
                e = lines[pos].split()
                if e[0] == "dir":
                    new_d = Dir(current, e[1], [])
                    current.dirs.append(new_d)
                    dirs.append(new_d)
                else:
                    current.dirsize += int(e[0])
                    cp = current
                    while cp.parent:
                        cp.parent.dirsize += int(e[0])
                        cp = cp.parent
                pos += 1

    else:
        current.dirsize += int(p[0])
        cp = current
        while cp.parent:
            cp.parent.dirsize += int(p[0])
            cp = cp.parent
        pos += 1

print("Puzzle 7.1:", sum(d.dirsize for d in dirs if d.dirsize <= 100000))

total = 70000000
needed = abs(total - dirs[0].dirsize - 30000000)

print("Puzzle 7.2:", min(s.dirsize for s in dirs if s.dirsize >= needed))
