import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

input = pd.read_csv('input.csv', header=None)
input = input[0].apply(lambda x: pd.Series(list(x))) # split strings into columns
simInput = input.copy()

def locate_in_df(df, value):
    a = df.to_numpy()
    row = np.where(a == value)[0][0]
    col = np.where(a == value)[1][0]
    return row, col

guard = '^'
potential_directions = ['^', '>', 'v', '<']
direction_ind = 0
potential_increments = [[-1, 0],\
                        [0, 1],\
                        [1,0],\
                        [0, -1]]
incr_i, incr_j = potential_increments[0] # when the guard is facing upwards, move updwards
pos_i, pos_j = locate_in_df(input, guard) 
len_x, len_y = np.shape(input)

potential_locations = []
while 0 <= pos_i + incr_i < len_x and 0 <= pos_j + incr_j < len_y:    

    if input.iloc[pos_i + incr_i, pos_j + incr_j] == '.' or input.iloc[pos_i + incr_i, pos_j + incr_j] == 'X':        

        if [int(pos_i), int(pos_j)] not in potential_locations:
            potential_locations.append([int(pos_i), int(pos_j)])

        input.iloc[pos_i, pos_j] = 'X'
        input.iloc[pos_i + incr_i, pos_j + incr_j] = guard        
        
        pos_i += incr_i
        pos_j += incr_j
        
    elif input.iloc[pos_i + incr_i, pos_j + incr_j] == '#':

        direction_ind = np.mod((direction_ind + 1), len(potential_directions))
        guard = potential_directions[direction_ind]
        incr_i, incr_j = potential_increments[direction_ind]

        input.iloc[pos_i, pos_j] = guard

# Add the final location if not already visited
if [int(pos_i), int(pos_j)] not in potential_locations: 
    potential_locations.append([int(pos_i), int(pos_j)])

def checkLocation(simInput, location, potential_directions, potential_increments):

    guard = '^'
    direction_ind = 0
    incr_i, incr_j = potential_increments[0] # when the guard is facing upwards, move updwards
    pos_i, pos_j = locate_in_df(simInput, guard) 
    start_i, start_j = pos_i, pos_j
    len_x, len_y = np.shape(simInput)

    visited_locations = []
    simInput.iloc[location[0], location[1]] = '#'
    
    while 0 <= pos_i + incr_i < len_x and 0 <= pos_j + incr_j < len_y:

        if simInput.iloc[pos_i + incr_i, pos_j + incr_j] == '.' or simInput.iloc[pos_i + incr_i, pos_j + incr_j] == 'X':       

            simInput.iloc[pos_i, pos_j] = 'X'
            simInput.iloc[pos_i + incr_i, pos_j + incr_j] = guard        
            
            pos_i += incr_i
            pos_j += incr_j
            
            if [pos_i, pos_j, guard] in visited_locations:
                return True

            visited_locations.append([pos_i, pos_j, guard])
            
        elif simInput.iloc[pos_i + incr_i, pos_j + incr_j] == '#':

            direction_ind = np.mod((direction_ind + 1), len(potential_directions))
            guard = potential_directions[direction_ind]
            incr_i, incr_j = potential_increments[direction_ind]

            simInput.iloc[pos_i, pos_j] = guard
    
    return False

output = 0
count = 0
for location in potential_locations:

    print(count)
    good = checkLocation(simInput.copy(), location, potential_directions, potential_increments)

    if good:
        output += 1

    count += 1

print(f"There are {output} possible locations for the obstacle.")