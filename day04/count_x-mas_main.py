import numpy as np 
import re
import pandas as pd

input = pd.read_csv('input.csv', header=None)
input = input[0].apply(lambda x: pd.Series(list(x))) # split strings into columns

output = 0

for i in range(1, len(input) - 1):
    for j in range(1, len(input) - 1):
        if input.iloc[i,j] == 'A':
            
            pattern1 = (input.iloc[i-1,j-1] == 'M' and input.iloc[i-1,j+1] == 'S') and \
                    (input.iloc[i+1,j-1] == 'M' and input.iloc[i+1,j+1] == 'S')

            pattern2 = (input.iloc[i-1,j-1] == 'S' and input.iloc[i-1,j+1] == 'M') and \
                    (input.iloc[i+1,j-1] == 'S' and input.iloc[i+1,j+1] == 'M')

            pattern3 = ((input.iloc[i-1,j-1] == 'S' and input.iloc[i-1,j+1] == 'S') and \
                        (input.iloc[i+1,j-1] == 'M' and input.iloc[i+1,j+1] == 'M')) 
            
            pattern4 = ((input.iloc[i-1,j-1] == 'M' and input.iloc[i-1,j+1] == 'M') and \
                        (input.iloc[i+1,j-1] == 'S' and input.iloc[i+1,j+1] == 'S'))

            if pattern1 or pattern2 or pattern3 or pattern4:
                output += 1

print(f"There are {output} occurrences of X-MAS")