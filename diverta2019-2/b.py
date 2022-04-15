n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(1)
    exit()

pq = set()
for i in range(n):
    for j in range(n):
        if i != j:
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            p, q = x1 - x2, y1 - y2
            pq.add((p, q))

INF = 10 ** 18
ans = INF
for p, q in pq:
    vis = set()
    cost = 0
    for x, y in xy:
        vis.add((x + p, y + q))
    for x, y in xy:
        if (x, y) not in vis:
            cost += 1
    ans = min(ans, cost)

print(ans)
