lines = open("inp_day7.txt").read()
lines = [line for line in lines.split("\n")]

from collections import defaultdict
filesystem = defaultdict(int)
directory = []

for line in lines:
    commands = line.split()
    if commands[1] == "cd":
        if commands[2] == "..":
            directory.pop()
        else:
            directory.append(commands[2])
    elif commands[1] == "ls":
        continue
    elif commands[0].isdigit():
        file_size = int(commands[0])
        for i in range(len(directory)):
            filesystem['/'.join(directory[:i + 1])] += file_size

values = list(filesystem.values())

large = []
for nr in values:
    if int(nr) < 100000:
        large.append(int(nr))

print(sum(large))

# Part 2
used_space = values[0]
unused_space = 70000000 - used_space
free_space = 30000000 - unused_space

candidates = []
for nr in values:
    if nr >= free_space:
        candidates.append(nr)

print(min(candidates))