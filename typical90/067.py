import numpy as np

N, K = input().split()

x = N
for _ in range(int(K)):
    x = str(np.base_repr(int(x, 8), 9)).replace("8", "5")

print(x)
