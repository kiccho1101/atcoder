import numpy as np

H, W = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(H)])
B = np.array([list(map(int, input().split())) for _ in range(H)])

C = B - A

ope_count = 0
for h in range(H - 1):
    for w in range(W - 1):
        if C[h][w] != 0:
            diff = -C[h][w]
            C[h][w] += diff
            C[h][w + 1] += diff
            C[h + 1][w] += diff
            C[h + 1][w + 1] += diff
            ope_count += abs(diff)


convertible = not np.any(C != 0)
if convertible:
    print("Yes")
    print(ope_count)
else:
    print("No")
