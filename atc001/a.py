import sys

sys.setrecursionlimit(10 ** 6)


class Solver:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.field = [list(input()) for _ in range(self.h)]
        self.ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.ans = False
        self.vis = [[False] * self.w for _ in range(self.h)]

    def dfs(self, y, x):
        if self.vis[y][x]:
            return
        self.vis[y][x] = True
        for dy, dx in self.ds:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < self.h and 0 <= nx < self.w:
                if self.field[ny][nx] == "g":
                    self.ans = True
                    return
                if self.field[ny][nx] == ".":
                    self.dfs(ny, nx)

    def solve(self):
        start_y = None
        start_x = None
        for y in range(self.h):
            for x in range(self.w):
                if self.field[y][x] == "s":
                    start_y = y
                    start_x = x
                    break
            else:
                continue
            break

        assert start_y is not None and start_x is not None
        self.dfs(start_y, start_x)
        if self.ans:
            print("Yes")
        else:
            print("No")


Solver().solve()
