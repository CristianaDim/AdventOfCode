import pandas as pd
import numpy as np

input = np.genfromtxt('input.csv', dtype=str)
len_x, len_y = len(input), len(input[0])   

node_locations = []
for i in range(len_x):
    for j in range(len_y):
        if input[i][j] != '.':
            node_locations.append([i, j, input[i][j]])
    
antenna_types = np.unique([node_locations[i][2] for i in range(len(node_locations))])

output = 0
unique_locations = []
for antenna in antenna_types:

    antenna_locations = [node_locations[i][0:2] for i in range(len(node_locations)) if node_locations[i][2] == antenna]

    if len(antenna_locations) > 1:
        for loc in antenna_locations:
            if loc not in unique_locations:
                output += 1
                unique_locations.append(loc)

        for ind1 in range(len(antenna_locations)):           
            for ind2 in range(ind1 + 1, len(antenna_locations)): 
                loc1, loc2 = antenna_locations[ind1], antenna_locations[ind2]
                x_diff, y_diff = [loc1[i] - loc2[i] for i in range(len(loc1))]                

                new_loc1 = [loc1[0] + x_diff, loc1[1] + y_diff]
                new_loc2 = [loc2[0] - x_diff, loc2[1] - y_diff]
                while new_loc1[0] >= 0 and new_loc1[0] < len_x and new_loc1[1] >= 0 and new_loc1[1] < len_y:
                    if new_loc1 not in unique_locations:
                        output += 1
                        unique_locations.append(new_loc1)
                    new_loc1 = [new_loc1[0] + x_diff, new_loc1[1] + y_diff]

                while new_loc2[0] >= 0 and new_loc2[0] < len_x and new_loc2[1] >= 0 and new_loc2[1] < len_y:
                    if new_loc2 not in unique_locations:
                        output += 1
                        unique_locations.append(new_loc2)
                    new_loc2 = [new_loc2[0] - x_diff, new_loc2[1] - y_diff]

print(f"There are {output} unique locations.")