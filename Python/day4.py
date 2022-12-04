lines = [line.strip() for line in open("aoc_4.txt")]
fully_covered = 0
overlap = 0
for line in lines:
    comp1, comp2 = line.split(",")
    s1, e1 = comp1.split("-")
    s2, e2 = comp2.split("-")
    s1, e1, s2, e2 = [int(nr) for nr in [s1, e1, s2, e2]]
    # Part 1
    if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
        fully_covered += 1
    # Part 2
    if not(e1 < s2 or e2 < s1):
        overlap += 1
print(fully_covered)
print(overlap)