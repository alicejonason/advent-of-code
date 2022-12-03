# Part 1
import string
letters = list(string.ascii_lowercase)
points = {}
for letter in letters:
    points[letter] = letters.index(letter) + 1
    points[letter.upper()] = letters.index(letter) + 27
    
lines = [line.strip() for line in open("aoc_3.txt")]
priority = 0
for line in lines:
    comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
    for letter in comp1:
        if letter in comp2:
            comp2 = comp2.replace(letter, '')
            priority += points[letter]
print(priority)

# Part 2
priority = 0
lines = [line.strip() for line in open("aoc_3.2.txt")]
for i in range(0, len(lines), 3):
    comp1, comp2, comp3 = lines[i], lines[i + 1], lines[i + 2]
    for letter in comp1:
        if letter in comp2 and letter in comp3:
            comp1 = comp1.replace(letter, '')
            comp2 = comp2.replace(letter, '')
            comp3 = comp3.replace(letter, '')
            priority += points[letter]
print(priority)