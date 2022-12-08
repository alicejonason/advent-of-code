import numpy as np

# Reading data
input = [line.strip() for line in open("day8.txt")]
forest = [list(map(int, list(line))) for line in input]
n_row = len(forest) 
n_col = len(forest[0]) 
forest = np.array(forest)

# Part 1
visible = 0
for r in range(n_row):
    for c in range(n_col):
        tree = forest[r, c]
        if c == 0 or tree > np.amax(forest[r, :c]):
            visible += 1
        elif c == n_col - 1 or tree > np.amax(forest[r, (c + 1):]):
            visible += 1
        elif r == 0 or tree > np.amax(forest[:r, c]):
            visible += 1
        elif r == n_row - 1 or tree > np.amax(forest[(r + 1):, c]):
            visible += 1

print("Visible: ", visible)

# Part 2
def view_dist(tree, direction):
    view_dist = 0
    for i in range(len(direction)):
        try:
            if direction[i] >= tree: 
                return(view_dist + 1)
            else: 
                view_dist += 1
        except IndexError:
            pass
    return(view_dist)

scenic_score = []
for r in range(n_row):
    for c in range(n_col):
        tree = forest[r, c]
        up = list(forest[:r, c])
        if len(up) >= 2:
            up.reverse()
        left = list(forest[r, :c])
        if len(left) >= 2:
            left.reverse()
        down = list(forest[(r + 1):, c])
        right = list(forest[r, (c + 1):])

        ss = (view_dist(tree, up) *
             view_dist(tree, left) * 
             view_dist(tree, down) * 
             view_dist(tree, right))
        scenic_score.append(ss)

print("Max scenic score: ", max(scenic_score))
