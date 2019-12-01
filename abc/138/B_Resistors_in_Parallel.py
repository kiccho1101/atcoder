import numpy as np

N = input()
A = np.array(input().split()).astype(int)
result = 0
for a in A:
    result += 1 / a
print(1 / result)
