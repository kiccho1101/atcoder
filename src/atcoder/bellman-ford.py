# Bellman-Ford
# https://kuruton.hatenablog.com/entry/2020/11/23/080000

from typing import List


def bellman_ford(edges: List[List[int]], V: int, start: int) -> List[int]:
    INF = 10 ** 18
    dist = [INF] * V
    dist[start] = 0
    E = len(edges)

    for i in range(V):
        for j in range(E):
            s, e, w = edges[j]
            if dist[s] != INF and dist[e] > dist[s] + w:
                dist[e] = dist[s] + w

                # n回目にも更新があるなら負の閉路がある
                if i == V - 1:
                    dist[e] = -INF
                    updated = True
                    while updated:
                        updated = False
                        for ss, ee, ww in edges:
                            if dist[ee] != -INF and dist[ss] == -INF:
                                dist[ee] = -INF
                                updated = True

    return dist


if __name__ == "__main__":
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    print(bellman_ford(edges, V, 0))

"""
input:
7 20
0 1 2
1 0 2
0 2 5
2 0 5
1 2 4
2 1 4
1 3 6
3 1 6
1 4 10
4 1 10
2 3 2
3 2 2
3 5 1
5 3 1
4 5 3
5 4 3
4 6 5
6 4 5
5 6 9
6 5 9

output:
[0, 2, 5, 7, 11, 8, 16]
"""


"""
input:
6 7
0 1 2
0 3 4
1 2 3
2 3 5
2 5 2
4 2 -4
5 4 1

output:
[0, 2, -inf, -inf, -inf, -inf]
"""
