import numpy as np
import time

input = list(np.genfromtxt('input.txt', delimiter=' '))
startTime = time.time()

for iter in range(75):
    print(f"Iteration {iter}, elapsed time: {(time.time() - startTime) / 60}")
    ind = 0
    totalLength = len(input)
    while ind < totalLength:

        if input[ind] == 0:
            input[ind] = 1

        elif len(str(input[ind])) % 2 == 0:
            string = str(int(input[ind]))
            length = len(string)

            num1, num2 = int(string[:int(length/2)]), int(string[int(length/2):])
            input.pop(ind)
            input.insert(ind, num1)
            input.insert(ind + 1, num2)
            ind += 1
            totalLength = len(input)

        else:
            input[ind] *= 2024
        
        ind += 1
    
print(f"The total number of stones is {len(input)}.")