import heapq

N = int(input())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dijkstra(graph, s):
    INF = 10 ** 18
    dist = [INF] * N
    visited = [False] * N
    queue = []
    dist[s] = 0
    heapq.heappush(queue, (0, s))
    while queue:
        d, v = heapq.heappop(queue)
        if visited[v]:
            continue
        visited[v] = True
        for to in graph[v]:
            d = dist[v] + 1
            if d < dist[to]:
                dist[to] = d
                heapq.heappush(queue, (d, to))
    return dist


dist_1 = dijkstra(graph, 0)
max_1 = dist_1.index(max(dist_1))
dist_2 = dijkstra(graph, max_1)

print(max(dist_2) + 1)
