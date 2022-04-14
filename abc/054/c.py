class Solver:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.graph = [[] for _ in range(self.n)]
        for _ in range(self.m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.ans = 0

    def dfs(self, x, vis):
        if sum(vis) == self.n:
            self.ans += 1
            return
        for to in self.graph[x]:
            if vis[to]:
                continue
            vis[to] = True
            self.dfs(to, vis)
            vis[to] = False

    def solve(self):
        vis = [False] * self.n
        vis[0] = True
        self.dfs(0, vis)
        print(self.ans)


Solver().solve()
