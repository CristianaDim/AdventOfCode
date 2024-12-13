import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

input = pd.read_csv('input.csv', header=None)
input = input[0].apply(lambda x: pd.Series(list(x))) # split strings into columns

def locate_in_df(df, value):
    a = df.to_numpy()
    row = np.where(a == value)[0][0]
    col = np.where(a == value)[1][0]
    return row, col

output = 1 # include the start
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

while 0 <= pos_i + incr_i < len_x and 0 <= pos_j + incr_j < len_y:    

    if input.iloc[pos_i + incr_i, pos_j + incr_j] == '.' or input.iloc[pos_i + incr_i, pos_j + incr_j] == 'X':

        if input.iloc[pos_i + incr_i, pos_j + incr_j] != 'X':
            output += 1

        input.iloc[pos_i, pos_j] = 'X'
        input.iloc[pos_i + incr_i, pos_j + incr_j] = guard        
        
        pos_i += incr_i
        pos_j += incr_j
        
    elif input.iloc[pos_i + incr_i, pos_j + incr_j] == '#':
        direction_ind = np.mod((direction_ind + 1), len(potential_directions))
        guard = potential_directions[direction_ind]
        incr_i, incr_j = potential_increments[direction_ind]

        input.iloc[pos_i, pos_j] = guard

print(f"The guard has visited {output} unique positions.")

fig, ax = plt.subplots(figsize=(10, 10))

for i in range(input.shape[0]):
    for j in range(input.shape[1]):
        ax.text(j, i, input.iloc[i, j], ha='center', va='center', fontsize=4)

ax.set_xlim(-0.5, input.shape[1] - 0.5)
ax.set_ylim(-0.5, input.shape[0] - 0.5)
ax.set_xticks([])
ax.set_yticks([])
ax.invert_yaxis()  
ax.set_aspect('equal')  

plt.savefig('GuardPath.svg', bbox_inches='tight', dpi=150)