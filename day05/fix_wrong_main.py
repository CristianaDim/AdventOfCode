import numpy as np

rules, updates = [], []
with open('input.txt', 'r+') as f:
    for line in f.readlines():
        if '|' in line.strip():
            rules.append(list(map(int,line.strip().split('|'))))
        elif line.strip() != '':
            updates.append(list(map(int,line.strip().split(','))))

def checkOrder(update):
    corrected = False
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            pair = [update[ind] for ind in [i,j]]
            if pair not in rules:
                v1 = update[i]
                v2 = update[j]
                update[i] = v2
                update[j] = v1
                corrected = True
                checkOrder(update)
    return update, corrected

output = 0
for update in updates:
    update, corrected = checkOrder(update)
    if corrected:
        output += update[int(len(update) / 2)]

print(f"The sum of the middle page numbers in the corrected updates is {output}.")
