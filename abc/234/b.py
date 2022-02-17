import math


N = int(input())
cords = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(len(cords) - 1):
    for j in range(i, len(cords)):
        xi, yi = cords[i]
        xj, yj = cords[j]
        dist = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
        ans = max(ans, dist)

print(ans)
