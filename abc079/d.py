import collections
from heapq import heappop, heappush

n = 10
h, w = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

nums = collections.defaultdict(int)
for _ in range(h):
    for a in map(int, input().split()):
        if a != -1 and a != 1:
            nums[a] += 1

INF = 10 ** 18
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            graph[i].append((j, mat[i][j]))


def dijkstra(graph, s):
    dist = [INF] * n
    dist[s] = 0
    queue = []
    heappush(queue, (0, s))
    while queue:
        d, fr = heappop(queue)
        for to, c in graph[fr]:
            if dist[fr] != INF and dist[to] > dist[fr] + c:
                dist[to] = dist[fr] + c
                heappush(queue, (dist[to], to))

    return dist


dists = [INF] * n
for i in range(n):
    dist = dijkstra(graph, i)
    dists[i] = dist[1]

ans = 0
for key in nums.keys():
    ans += nums[key] * dists[key]

print(ans)
