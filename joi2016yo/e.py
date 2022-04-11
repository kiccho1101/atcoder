from heapq import heappop, heappush
import collections
from operator import is_

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())

has_zombie = [False] * N
for _ in range(K):
    c = int(input())
    c -= 1
    has_zombie[c] = True

graph = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    graph[s].append(e)
    graph[e].append(s)

is_dangerous = [False] * N
queue = collections.deque([(c, 0) for c in range(N) if has_zombie[c]])
vis = [False] * N
while queue:
    s, d = queue.popleft()
    if vis[s]:
        continue
    vis[s] = True
    is_dangerous[s] = True
    for to in graph[s]:
        if d + 1 <= S:
            queue.append((to, d + 1))


INF = 10 ** 18
dist = [INF] * N
dist[0] = 0
queue = []
heappush(queue, (0, 0))
while queue:
    c, s = heappop(queue)
    if dist[s] != INF:
        for e in graph[s]:
            if has_zombie[e]:
                continue
            if is_dangerous[e]:
                if dist[e] > dist[s] + Q:
                    dist[e] = dist[s] + Q
                    heappush(queue, (dist[e], e))
            else:
                if dist[e] > dist[s] + P:
                    dist[e] = dist[s] + P
                    heappush(queue, (dist[e], e))


ans = dist[N - 1]
if is_dangerous[N - 1]:
    ans -= Q
else:
    ans -= P
print(ans)
