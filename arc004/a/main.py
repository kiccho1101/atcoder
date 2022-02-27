import math


N = int(input())

xs = []
ys = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        xi = xs[i]
        yi = ys[i]
        xj = xs[j]
        yj = ys[j]

        dist = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
        ans = max(ans, dist)

print(ans)
