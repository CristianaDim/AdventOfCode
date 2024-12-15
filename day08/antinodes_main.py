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
        for ind1 in range(len(antenna_locations)):           
            for ind2 in range(ind1 + 1, len(antenna_locations)): 
                x_diff, y_diff = [antenna_locations[ind1][i] - antenna_locations[ind2][i] for i in range(len(antenna_locations[ind1]))]
                
                new_loc1 = [antenna_locations[ind1][0] + x_diff, antenna_locations[ind1][1] + y_diff]
                new_loc2 = [antenna_locations[ind2][0] - x_diff, antenna_locations[ind2][1] - y_diff]

                for new_loc in [new_loc1, new_loc2]:
                    if new_loc not in unique_locations and new_loc[0] >= 0 and new_loc[1] >= 0 and new_loc[0] < len_x and new_loc[1] < len_y:
                            output += 1
                            unique_locations.append(new_loc)

print(f"There are {output} unique locations.")