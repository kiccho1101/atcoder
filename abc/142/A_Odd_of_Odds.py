import numpy as np

N = int(input())
print(np.mean([*map(lambda x: x % 2, np.arange(1, N + 1))]))
