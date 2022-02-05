N, K = map(int, input().split())

hs = list(map(int, input().split()))

graph = [[] for _ in range(len(hs))]
for i in range(len(hs)):
    for j in range(1, K + 1):
        if i - j >= 0:
            graph[i].append(abs(hs[i - j] - hs[i]))


INF = 10 ** 10
dist = [INF] * len(hs)
dist[0] = 0
for i in range(len(hs)):
    min_dist = INF

    for j in range(len(graph[i])):
        d = dist[i - j - 1] + graph[i][j]
        if d < min_dist:
            min_dist = d

    if min_dist != INF:
        dist[i] = min_dist

print(dist[-1])
