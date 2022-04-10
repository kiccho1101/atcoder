from heapq import heappop, heappush
import math

INF = 10 ** 18
N, M, K = map(int, input().split())
ts = [int(input()) for _ in range(N - 2)]
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))


dist = [INF] * N
dist[0] = 0
queue = []
heappush(queue, (0, 0))
while queue:
    w, fr = heappop(queue)
    for to, c, d in graph[fr]:
        curr = dist[fr]
        if 0 < fr < N - 1:
            curr += ts[fr - 1]
        start_t = d * math.ceil(curr / d)
        if dist[fr] != INF and dist[to] > start_t + c:
            dist[to] = start_t + c
            heappush(queue, (dist[to], to))


ans = dist[N - 1]
if ans <= K:
    print(ans)
else:
    print(-1)
