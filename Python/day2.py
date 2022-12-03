# Part 1
lines = [line.strip() for line in open("aoc_2.txt")]
points = {"X": 1, "Y": 2, "Z": 3}
score = {"A": {"X": 3, "Y": 6, "Z": 0}, 
        "B": {"X": 0, "Y": 3, "Z": 6}, 
        "C": {"X": 6, "Y": 0, "Z": 3}}
total = 0
for line in lines:
    in1, in2 = line.split()
    total += int(points[in2]) + int(score[in1][in2])
print(total)

# Part 2
new_move = {"A": {"X": "Z", "Y": "X", "Z": "Y"},
            "B": {"X": "X", "Y": "Y", "Z": "Z"},
            "C": {"X": "Y", "Y": "Z", "Z": "X"}}
total = 0
for line in lines:
    in1, in2 = line.split()
    total += int(points[new_move[in1][in2]]) + int(score[in1][new_move[in1][in2]])
print(total)