import numpy as np

s = np.array(input().split()).astype(int).sum()
if s >= 22:
    print("bust")
else:
    print("win")
