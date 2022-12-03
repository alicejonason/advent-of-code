# Part 1
def calories(f):
    elf = 0
    calories = []
    lines = [lines.strip() for lines in open("aoc_1.txt")]
    for line in lines:
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