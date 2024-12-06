import numpy as np
import re
with open('input.txt', 'r') as f:
    input = f.readlines()

output = 0
for ind in range(len(input)):
    operands = re.findall(r'mul\([0-9]+\,[0-9]+\)', input[ind])
    for operand in operands:
        extracted = operand[4:-1].split(',')
        output += int(extracted[0]) * int(extracted[1])

print(f"The result is: {output}")