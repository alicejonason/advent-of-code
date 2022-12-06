def aoc_6(text, nr):
    for i in range(nr, len(text)):
        marker = text[i-nr:i]
        unique = ""
        for j in marker:
            if j not in unique:
                unique += j
        if len(unique) == nr:
            return(i)

print(aoc_6(open("inp_day6.txt").read(), 4))  # Part 1
print(aoc_6(open("inp_day6.txt").read(), 14)) # Part 2