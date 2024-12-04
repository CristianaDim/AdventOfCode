import numpy as np

input = np.loadtxt('input.csv')

totalSimilarity = 0

for i in range(np.shape(input)[0]):
    totalSimilarity += input[i,0] * np.shape(np.where(input[:, 1] == input[i,0]))[1]

print(f"The similarity between the two lists is: {int(totalSimilarity)}")
