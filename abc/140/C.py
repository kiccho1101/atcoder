import numpy as np

N = input()
B = np.array(input().split()).astype(int)
B_left = np.insert(B, 0, B[0])
B_right = np.insert(B, len(B) - 1, B[-1])
print(np.min(np.array([B_left, B_right]).T, axis=1).sum())
