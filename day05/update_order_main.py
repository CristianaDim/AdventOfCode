import numpy as np

rules, updates = [], []
with open('input.txt', 'r+') as f:
    for line in f.readlines():
        if '|' in line.strip():
            rules.append(list(map(int,line.strip().split('|'))))
        elif line.strip() != '':
            updates.append(list(map(int,line.strip().split(','))))

output = 0
for update in updates:
    pairs = []
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            pairs.append([update[ind] for ind in [i,j]])

    correct = True
    for pair in pairs:
        if pair not in rules:
            correct = False
            break
    
    if correct:
        output += update[int(len(update) / 2)]

print(f"The sum of the middle page numbers is {output}.")