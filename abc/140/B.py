import numpy as np

N = int(input())
A = np.array(input().split()).astype(int)
B = np.array(input().split()).astype(int)
C = np.array(input().split()).astype(int)
r = sum(B)
r += C[A[np.append(np.diff(A) == 1, False)] - 1].sum()
print(r)
