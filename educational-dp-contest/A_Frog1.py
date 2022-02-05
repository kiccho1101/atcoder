_ = input()
hs = list(map(int, input().split()))

graph = [[] for _ in range(len(hs))]
for i in range(len(hs)):
    if i >= 1:
        graph[i].append(abs(hs[i - 1] - hs[i]))
    if i >= 2:
        graph[i].append(abs(hs[i - 2] - hs[i]))

INF = 10 ** 10
dist = [INF] * len(hs)
dist[0] = 0
for i in range(len(hs)):
    if len(graph[i]) == 1:
        dist[i] = dist[i - 1] + graph[i][0]
    if len(graph[i]) == 2:
        dist[i] = min(dist[i - 1] + graph[i][0], dist[i - 2] + graph[i][1])

print(dist[-1])
