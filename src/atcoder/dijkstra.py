import heapq
from typing import List, Tuple
# https://atcoder.jp/contests/typical90/tasks/typical90_m


def dijkstra(graph: List[List[Tuple[int, int]]], s: int) -> List[int]:
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    queue = []
    dist[s] = 0
    heapq.heappush(queue, (0, s))
    while queue:
        d, v = heapq.heappop(queue)
        for to, c in graph[v]:
            if dist[v] != INF and dist[to] > dist[v] + c:
                dist[to] = dist[v] + c
                heapq.heappush(queue, (dist[to], to))
    return dist


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))

    dist = dijkstra(graph, 0)
    print(dist)


"""
input:
7 9
1 2 2
1 3 3
2 5 2
3 4 1
3 5 4
4 7 5
5 6 1
5 7 6
6 7 3

output:
[0, 2, 3, 4, 4, 5, 8]
"""
