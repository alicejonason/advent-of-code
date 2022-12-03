# Part 1
def calories(f):
    elf = 0
    calories = []
    with open(f) as f_in:
        lines = f_in.readlines()
        for line in lines:
            line = line.strip()
            if line != '':
                elf += int(line)
                continue
            else:
                calories.append(elf)
                elf = 0
        return(calories)

print(max(calories("aoc_1.txt")))

# Part 2
print(sum(sorted(calories("aoc_1.txt"), reverse = True)[0:3]))
