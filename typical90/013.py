import heapq


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))


def dijkstra(s, N, graph):
    INF = 10 ** 18
    dist = [INF] * N
    visited = [False] * N
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        v = heapq.heappop(q)[1]
        if visited[v]:
            continue
        visited[v] = True
        for p, c in graph[v]:
            if visited[p]:
                continue
            d = dist[v] + c
            if d < dist[p]:
                dist[p] = d
                heapq.heappush(q, (dist[p], p))

    return dist


dist_0 = dijkstra(0, N, graph)
dist_1 = dijkstra(N - 1, N, graph)

for i in range(len(dist_0)):
    ans = dist_0[i] + dist_1[i]
    print(ans)
