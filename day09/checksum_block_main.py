import numpy as np

with open('input.txt', 'r+') as f:
    for line in f.readlines():
        input = line.strip()

count = 0
converted = []

for i in range(0, len(input) - 1, 2):
    l = []
    for c in range(int(input[i])):
        l.append(str(count))
    converted.append(l)
    l = []
    for c in range(int(input[i+1])):
        l.append('.')
    converted.append(l)
    
    count += 1
    
if len(input) % 2 == 1:
    l = []
    for c in range(int(input[-1])):
        l.append(str(count))
    converted.append(l)

def find_fit(converted, free_spaces, length):
    ind = 0
    while len(converted[free_spaces[ind]]) < length:
        ind += 1
    
    return free_spaces[ind]

free_spaces = [i for i in range(len(converted)) if '.' in converted[i]]
largest_space = np.max([len(converted[i]) for i in free_spaces])

ind_number = len(converted) - 1
ind_free = free_spaces[0]

id = int(converted[-1][-1])
ind_number = [i for i in range(len(converted)) if str(id) in converted[i]][0]
while id > 0:
    print(id)
    curr_len = len(converted[ind_number])

    if curr_len > largest_space:
        id -= 1
        ind_number = [i for i in range(len(converted)) if str(id) in converted[i]][0]
        continue
    
    fit = find_fit(converted, free_spaces, curr_len)
    if fit > ind_number:
        id -= 1
        ind_number = [i for i in range(len(converted)) if str(id) in converted[i]][0]
        continue

    a = converted[fit][:len(converted[ind_number])]
    converted.insert(fit, converted[ind_number])
    [converted[fit+1].pop(0) for i in a]
    converted[ind_number+1] = a
    id -= 1
    ind_number = [i for i in range(len(converted)) if str(id) in converted[i]][0]

    free_spaces = [i for i in range(len(converted)) if '.' in converted[i]]
    largest_space = np.max([len(converted[i]) for i in free_spaces])
    first_largest_space = np.argmax([len(converted[i]) for i in free_spaces])

c = []
for i in range(len(converted)):
    for j in range(len(converted[i])):
            c.append(converted[i][j])

checksum = 0
count = 0

while len(c) > 0:
    number = c.pop(0)
    if number != '.':
        checksum += int(number) * count
        count += 1
        
    else:
        count += 1

print(f"The checksum is {checksum}.")