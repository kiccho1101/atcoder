import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(graph, s, N):
    INF = 10 ** 18
    dist = [INF] * N
    dist[s] = 0
    visited = [False] * N

    queue = []
    heapq.heappush(queue, (0, s))

    while queue:
        c, v = heapq.heappop(queue)
        if visited[v]:
            continue
        visited[v] = True
        for to, c in graph[v]:
            d = dist[v] + c
            if d < dist[to]:
                dist[to] = d
                heapq.heappush(queue, (d, to))

    return dist


dist1 = dijkstra(graph, 0, N)
dist2 = dijkstra(graph, N - 1, N)

for i in range(len(dist1)):
    ans = dist1[i] + dist2[i]
    print(ans)
