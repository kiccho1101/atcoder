import heapq


N = int(input())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dijkstra(s, graph, N):
    INF = 10 ** 18
    dist = [INF] * N
    visited = [False] * N
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        v = heapq.heappop(q)[1]
        if visited[v]:
            continue
        visited[v] = True
        for i in graph[v]:
            if visited[i]:
                continue
            d = dist[v] + 1
            if dist[i] > d:
                dist[i] = d
                heapq.heappush(q, (d, i))
    return dist


dist_1 = dijkstra(0, graph, N)
max_i = dist_1.index(max(dist_1))
dist_2 = dijkstra(max_i, graph, N)

ans = max(dist_2) + 1
print(ans)
