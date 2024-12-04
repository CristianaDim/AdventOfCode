import numpy as np

input = np.loadtxt('input.csv')

totalDistance = 0

for i in range(np.shape(input)[0]):
    minCol0, minCol1 = np.nanmin(input, axis=0)[0], np.nanmin(input, axis=0)[1]
    locMin0, locMin1 = np.nanargmin(input, axis=0)[0], np.nanargmin(input, axis=0)[1]

    totalDistance += np.absolute(minCol1 - minCol0)

    input[locMin0, 0] = np.nan
    input[locMin1, 1] = np.nan

print(f"The total distance is: {int(totalDistance)}") #3508942