import numpy as np

N = int(input())
result = []
for i in range(N + 1):
    for j in range(i, N + 1):
        if i * j == N:
            result.append(i + j - 2)
print(min(result))
