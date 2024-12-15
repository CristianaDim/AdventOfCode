import numpy as np

results, operands = [], []
with open('input.txt', 'r+') as f:
    for line in f.readlines():
        stripped = line.strip()
        split = stripped.split(': ')
        results.append(int(split[0]))
        operands.append([int(x) for x in split[1].split(' ')])

output = 0
operators = [0, 1, 2] # 0 = +
                   # 1 = *
                   # 2 = ||
for ind in range(len(results)):
    print(ind)
    no_operators = len(operands[ind]) - 1
    no_combinations = 3 ** no_operators

    operator_array = np.zeros((no_combinations, no_operators))
    for i in range(np.shape(operator_array)[0]):
        number = np.base_repr(i, base = 3, padding=np.shape(operator_array)[1])
        for j in range(np.shape(operator_array)[1]):
            operator_array[i][j] = number[-np.shape(operator_array)[1]:][j]
    
    for combination in operator_array:
        target = results[ind]
        values = operands[ind]
        check = values[0]
        for i in range(len(combination)):
            if combination[i] == 0:
                check += values[i + 1]
            elif combination[i] == 1:
                check *= values[i + 1]
            elif combination[i] == 2:
                check = int(str(check) + str(values[i+1]))
        
        if check == target:
            output += check
            break
        
print(f"The calibration result is {output}.")
