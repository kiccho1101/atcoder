import sys

sys.setrecursionlimit(10 ** 6)


class Solver:
    def __init__(self):
        self.n = int(input())
        self.A = [int(input()) for _ in range(self.n)]
        self.vis = [False] * self.n
        self.INF = 10 ** 18
        self.ans = self.INF

    def dfs(self, x, d):
        if self.vis[x]:
            return
        self.vis[x] = True
        if x == 1:
            self.ans = min(self.ans, d)
            return
        self.dfs(self.A[x] - 1, d + 1)

    def solve(self):
        self.dfs(0, 0)
        if self.ans == self.INF:
            print(-1)
        else:
            print(self.ans)


Solver().solve()
