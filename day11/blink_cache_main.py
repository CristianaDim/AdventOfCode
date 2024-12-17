import numpy as np
import time
from functools import lru_cache

input = list(np.genfromtxt('input.txt', delimiter=' '))
startTime = time.time()


def check_conditions(number):

    if number == 0:
        result = [1]

    elif len(str(number)) % 2 == 0:

        string = str(int(number))
        length = len(string)

        num1, num2 = int(string[:int(length/2)]), int(string[int(length/2):])
        result = [num1, num2]

    else:
        result = [number * 2024]

    return result

@lru_cache(maxsize=None)
def final_split_length(stones, nIter):
    if nIter == 0:
        return len(stones)

    return sum(final_split_length(tuple(check_conditions(stone)), nIter - 1) for stone in stones)

    
print(f"The total number of stones is {final_split_length(tuple(input), 75)}.")