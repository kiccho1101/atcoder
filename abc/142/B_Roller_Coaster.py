import numpy as np

N, K = input().split()
h = np.array(input().split()).astype(int)
print((h >= int(K)).astype(int).sum())
