import heapq

n, k = map(int, input().split())

ans = []
graph = [[] for _ in range(n)]
for _ in range(k):
    i = tuple(map(int, input().split()))

    if i[0] == 0:
        _, s, e = i
        s -= 1
        e -= 1
        INF = 10 ** 18
        dist = [INF] * n
        queue = []
        heapq.heappush(queue, (0, s))
        dist[s] = 0
        while queue:
            d, v = heapq.heappop(queue)
            if graph[v]:
                for to, c in graph[v]:
                    if dist[v] != INF and dist[to] > dist[v] + c:
                        dist[to] = dist[v] + c
                        heapq.heappush(queue, (dist[to], to))
        if dist[e] == INF:
            ans.append(-1)
        else:
            ans.append(dist[e])

    if i[0] == 1:
        _, c, d, e = i
        c -= 1
        d -= 1
        graph[c].append((d, e))
        graph[d].append((c, e))

for a in ans:
    print(a)
