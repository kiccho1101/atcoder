N = int(input())

xy = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if i != j and j != k and k != i:
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                S = (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)
                if S != 0:
                    ans += 1

print(ans)
