import numpy as np

N, M = map(int, input().split())

xs, ys, rs = [], [], []
for _ in range(N):
    x, y, r = map(int, input().split())
    xs.append(x)
    ys.append(y)
    rs.append(r)
for _ in range(M):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    rs.append(-1)

ans = 10e10
for i in range(N + M - 1):
    for j in range(i + 1, N + M):
        d = np.sqrt((xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2)
        min_d = 10e10
        if rs[i] != -1 and rs[j] != -1:
            min_d = min(rs[i], rs[j])
        elif rs[i] != -1:
            min_d = d - rs[i]
        elif rs[j] != -1:
            min_d = d - rs[j]
        else:
            min_d = d / 2

        if min_d < ans:
            ans = min_d

print(ans)
