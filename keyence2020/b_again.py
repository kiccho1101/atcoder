N = int(input())

points = []
for i in range(N):
    x, l = map(int, input().split())
    points.append((x - l, x + l))

points.sort(key=lambda x: x[1])

INF = 10 ** 18
curr = -INF
ans = 0
for first, second in points:
    if curr <= first:
        ans += 1
        curr = second

print(ans)
