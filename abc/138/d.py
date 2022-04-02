from collections import defaultdict

N, Q = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

counter = defaultdict(int)
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    counter[p] += x


class Solver:
    def __init__(self, N, counter, graph):
        self.visited = [False] * N
        self.counter = counter
        self.dp = [0] * N
        self.dp[0] = self.counter[0]
        self.graph = graph

    def dfs(self, pre, now):
        if self.visited[now]:
            return
        self.visited[now] = True
        self.dp[now] = counter[now]
        if pre != -1:
            self.dp[now] += self.dp[pre]
        for to in self.graph[now]:
            self.dfs(now, to)


solver = Solver(N, counter, graph)
solver.dfs(-1, 0)
print(*solver.dp)
