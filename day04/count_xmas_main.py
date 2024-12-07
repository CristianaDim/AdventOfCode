import numpy as np 
import re
import pandas as pd

input = pd.read_csv('input.csv', header=None)
input = input[0].apply(lambda x: pd.Series(list(x))) # split strings into columns

output = 0

def count(target, query):
    found = re.findall(r'' + re.escape(target), query)
    if found is not None:
        return len(found)
    return 0

# Get forward and backward occurrences on rows and columns (rows == columns, otherwise it wouldn't work)
for i in range(len(input)):   
    query = list(input[i].values) # columns
    query = ''.join(query)
    output += count('XMAS', query) + count('SAMX', query)

    query = list(input.iloc[i]) # rows
    query = ''.join(query)
    output += count('XMAS', query) + count('SAMX', query)

# Function to extract diagonals
def get_diagonals(matrix):
    diags = []
    rows, cols = len(matrix), len(matrix[0])
    for diag_start in range(-rows + 1, cols):
        diag = []
        for i in range(rows):
            j = i + diag_start
            if 0 <= j < cols:
                diag.append(matrix[i][j])
        diags.append("".join(diag))
    return diags

# Function to extract all diagonals from top-right to bottom-left
def get_anti_diagonals(matrix):
    diags = []
    rows, cols = len(matrix), len(matrix[0])
    for diag_start in range(cols + rows - 1):
        diag = []
        for i in range(rows):
            j = diag_start - i
            if 0 <= j < cols:
                diag.append(matrix[i][j])
        diags.append("".join(diag))
    return diags

# Check all diagonals and anti-diagonals
for diagonal in get_diagonals(input):
    output += count('XMAS', diagonal) + count('SAMX', diagonal)
    
for anti_diagonal in get_anti_diagonals(input):    
    output += count('XMAS', anti_diagonal) + count('SAMX', anti_diagonal)

print(f'There are {output} occurrences of XMAS')
