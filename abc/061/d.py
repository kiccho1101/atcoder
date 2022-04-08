N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, -c))

INF = 10 ** 18
dist = [INF] * N
dist[0] = 0
for i in range(N):
    for j in range(M):
        a, b, c = edges[j]
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c

            if i == N - 1:
                dist[b] = -INF
                updated = True
                for aa, bb, cc in edges:
                    if dist[bb] != -INF and dist[aa] == -INF:
                        dist[bb] = -INF
                        updated = True

if dist[N - 1] == -INF:
    print("inf")
else:
    print(-dist[N - 1])
