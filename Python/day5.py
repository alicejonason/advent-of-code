stacks = [
    ["F", "H", "B", "V", "R", "Q", "D", "P"],
    ["L", "D", "Z", "Q", "W", "V"],
    ["H", "L", "Z", "Q", "G", "R", "P", "C"],
    ["R", "D", "H", "F", "J", "V", "B"],
    ["Z", "W", "L", "C"],
    ["J", "R", "P", "N", "T", "G", "V", "M"],
    ["J", "R", "L", "V", "M", "B", "S"],
    ["D", "P", "J"],
    ["D", "C", "N", "W", "V"]]

stacks = [stack[::-1] for stack in stacks] 
procedure = [line.strip() for line in open("inp_day5.txt")]

for line in procedure:
    digits = line.split(" ")
    nr = int(digits[1]) - 1
    from_ = int(digits[3]) - 1
    to_ = int(digits[5]) - 1
    remove = stacks[from_][:nr + 1]
    keep = stacks[from_][nr + 1:]
    stacks[from_] = keep
    for element in reversed(remove): # For part 2, just change to reversed
        stacks[to_].insert(0, element)

for element in stacks:
    print(element[0])
