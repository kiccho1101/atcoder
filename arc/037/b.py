class Solver:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.graph = [[] for _ in range(self.n)]
        for _ in range(self.m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.vis = [False] * self.n

    def dfs(self, x, prev=-1):
        if self.vis[x]:
            return False
        self.vis[x] = True
        for to in self.graph[x]:
            if prev != to:
                if not self.dfs(to, x):
                    return False
        return True

    def solve(self):
        ans = 0
        for i in range(self.n):
            if not self.vis[i]:
                if self.dfs(i):
                    ans += 1
        print(ans)


Solver().solve()
