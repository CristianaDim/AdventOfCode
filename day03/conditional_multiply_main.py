import numpy as np
import re
with open('input.txt', 'r') as f:
    input = f.readlines()

def getInds(text):
    operands = re.search(r'mul\([0-9]+\,[0-9]+\)', text)
    if operands is not None:
        extracted = operands.group()[4:-1].split(',')
        return operands.span()[0], operands.span()[1], int(extracted[0]) * int(extracted[1])
    return None

output = 0
toAdd = True

for ind in range(len(input)):
    start = 0
    end = getInds(input[ind][start:])[0]

    while getInds(input[ind][start:]):
        
        out = getInds(input[ind][start:])
        end = start + out[0]
        
        if re.search(r'don\'t\(\)', input[ind][start:end]) is not None:
            toAdd = False
        if re.search(r'do\(\)', input[ind][start:end]) is not None:
            toAdd = True
        if toAdd:
            output += out[2]
        
        start += out[1]

print(f"The result is: {output}") #92082041