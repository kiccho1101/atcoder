# %%
import numpy as np

H, _ = map(int, input().split())

arr = np.array([list(map(int, input().split())) for _ in range(H)])


ans = np.zeros(arr.shape)

H, W = arr.shape

row_sum = np.sum(arr, axis=0)
col_sum = np.sum(arr, axis=1)

row_sums = np.array([row_sum for _ in range(H)])
col_sums = np.array([col_sum for _ in range(W)]).T

ans = row_sums + col_sums - arr

for a in ans:
    print(" ".join(map(str, a.astype(int))))
