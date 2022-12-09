import numpy as np

motions = [line.strip("\n").split() for line in open("day9.txt")]
grid = np.empty((1000, 1000), dtype = str)

h_row, h_col = len(grid) // 2, len(grid[0]) // 2
t_row, t_col = len(grid) // 2, len(grid[0]) // 2

t_positions = []
h_positions = []

t_positions.append([t_row, t_col])
h_positions.append([h_row, h_col])

for line in motions:
    # Moving H one position at a time
    for i in range(int(line[1])): 
        if line[0] == "R":
            h_col += 1
        elif line[0] == "L":
            h_col -= 1
        elif line[0] == "U":
            h_row -= 1
        elif line[0] == "D":
            h_row += 1
        h_positions.append([h_row, h_col])

        if h_row == t_row or h_col == t_col:
            if abs(h_col - t_col) == 2 or abs(h_row - t_row) == 2:
                if line[0] == "R":
                    t_col += 1
                elif line[0] == "L":
                    t_col -= 1
                elif line[0] == "U":
                    t_row -= 1
                elif line[0] == "D":
                    t_row += 1
        # If adjacent, stay put but save H:s last position
        elif [h_row, h_col] == [t_row - 1, t_col - 1] or \
                [h_row, h_col] == [t_row - 1, t_col + 1] or \
                [h_row, h_col] == [t_row + 1, t_col - 1] or \
                [h_row, h_col] == [t_row + 1, t_col + 1]:
            continue

        else:
            t_row, t_col = h_positions[-2][0], h_positions[-2][1]

        t_positions.append([t_row, t_col])

unique_positions = [list(pos) for pos in set(tuple(pos) for pos in t_positions)]
print(len(unique_positions))