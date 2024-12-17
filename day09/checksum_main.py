import numpy as np

with open('input.txt', 'r+') as f:
    for line in f.readlines():
        input = line.strip()

count = 0
converted = []
for i in range(0, len(input) - 1, 2):
    for c in range(int(input[i])):
        converted.append(str(count))
    for c in range(int(input[i+1])):
        converted.append('.')
    
    count += 1
if len(input) % 2 == 1:
    for c in range(int(input[-1])):
        converted.append(str(count))

free_spaces = [i for i in range(len(converted)) if converted[i] == '.']

ind_number = len(converted) - 1
ind_free = free_spaces.pop(0)
while free_spaces and ind_number >= ind_free:

    converted[ind_free] = converted[ind_number]
    converted[ind_number] = '.'

    ind_number -= 1
    while converted[ind_number] == '.':
        ind_number -= 1
    ind_free = free_spaces.pop(0)

checksum = 0
number = converted.pop(0)
count = 0

while number != '.':
    checksum += int(number) * count
    count += 1
    number = converted.pop(0)

print(f"The checksum is {checksum}.")