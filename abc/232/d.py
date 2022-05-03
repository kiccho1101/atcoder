class Solver:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.field = [list(input()) for _ in range(self.h)]
        self.ans = 0
        self.vis = [[-1] * self.w for _ in range(self.h)]

    def dfs(self, y, x, d):
        if self.vis[y][x] != -1:
            return self.vis[y][x]
        ans = d
        if 0 <= x + 1 < self.w and self.field[y][x + 1] == ".":
            ans = max(ans, self.dfs(y, x + 1, d + 1))
        if 0 <= y + 1 < self.h and self.field[y + 1][x] == ".":
            ans = max(ans, self.dfs(y + 1, x, d + 1))
        self.vis[y][x] = ans
        self.ans = max(self.ans, ans)
        return ans

    def solve(self):
        self.dfs(0, 0, 1)
        print(self.ans)


Solver().solve()
