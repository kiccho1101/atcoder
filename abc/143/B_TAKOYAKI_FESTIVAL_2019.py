import numpy as np

N = int(input())
d = np.array(input().split()).astype(int)
a = np.outer(d, d)
np.fill_diagonal(a, 0)
a = np.triu(a)
print(a.sum())
