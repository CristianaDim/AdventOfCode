import numpy as np

directions = [[-1, 0],\
              [1, 0],\
              [0, -1],\
              [0, 1]]
inp = np.loadtxt('input.csv', delimiter = None, dtype=str)

input = np.zeros((len(inp), len(inp[0])))
for i in range(len(inp)):
    for j in range(len(inp[i])):
        input[i][j] = int(inp[i][j])

def update_next_pos(start_x, start_y, input, directions, visited, next_pos):

    for d in directions:
        next_x, next_y = int(start_x + d[0]), int(start_y + d[1])
        if next_x >= 0 and next_x < len(input) and next_y >= 0 and next_y < len(input[0]) and [next_x, next_y] not in visited and \
            input[next_x][next_y] - input[start_x][start_y] == 1 and [next_x, next_y] not in next_pos:
            next_pos.append([next_x, next_y])
    return next_pos

def get_score(start_x, start_y, input, directions):

    score = 0
    visited = []
    visited.append([start_x, start_y])

    next_pos = []
    next_pos.append([start_x, start_y])

    while len(next_pos):
        curr_pos = next_pos.pop(0)
        
        if input[curr_pos[0]][curr_pos[1]] == 9:
            score += 1
        next_pos = update_next_pos(curr_pos[0], curr_pos[1], input, directions, visited, next_pos)    
        visited.append(curr_pos)

    return score

trailheads = np.where(input == 0)
output = 0
for i, j in zip(trailheads[0], trailheads[1]):
    print(i,j)

    output += get_score(i,j, input, directions)

print(f"The score of the trailheads is {output}.")