import heapq


class Solver:
    def __init__(self):
        self.n, self.m, self.s, self.t = map(int, input().split())
        self.s -= 1
        self.t -= 1
        self.graph_yen = [[] for _ in range(self.n)]
        self.graph_snuk = [[] for _ in range(self.n)]
        self.INF = 10 ** 18
        for _ in range(self.m):
            u, v, a, b = map(int, input().split())
            u -= 1
            v -= 1
            self.graph_yen[u].append((v, a))
            self.graph_yen[v].append((u, a))
            self.graph_snuk[u].append((v, b))
            self.graph_snuk[v].append((u, b))

    def dijkstra(self, graph, s):
        dist = [self.INF] * self.n
        dist[s] = 0
        queue = []
        heapq.heappush(queue, (0, s))
        while queue:
            d, fr = heapq.heappop(queue)
            for to, c in graph[fr]:
                if dist[fr] != self.INF and dist[to] > dist[fr] + c:
                    dist[to] = dist[fr] + c
                    heapq.heappush(queue, (dist[to], to))
        return dist

    def solve(self):
        dist_yen = self.dijkstra(self.graph_yen, self.s)
        dist_snuk = self.dijkstra(self.graph_snuk, self.t)
        ans = [-1] * self.n
        for i in reversed(range(self.n)):
            a = 10 ** 15 - (dist_yen[i] + dist_snuk[i])
            if i < self.n - 1:
                a = max(a, ans[i + 1])
            ans[i] = a
        for a in ans:
            print(a)


Solver().solve()
