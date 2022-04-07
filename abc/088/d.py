from collections import deque

INF = 10 ** 18


class Solver:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.field = [list(input()) for _ in range(self.h)]
        self.vis = set()
        self.ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(self):
        queue = deque()
        queue.append((0, 0, 0))
        vis = set()
        min_dis = INF
        while queue:
            y, x, d = queue.popleft()
            if (y, x) == (self.h - 1, self.w - 1):
                min_dis = min(min_dis, d)
            if (y, x) in vis:
                continue
            vis.add((y, x))
            for dy, dx in self.ds:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < self.h and 0 <= nx < self.w and self.field[ny][nx] != "#":
                    queue.append((ny, nx, d + 1))
        return min_dis

    def solve(self):
        min_dis = self.bfs()
        if min_dis == INF:
            print(-1)
        else:
            black_count = 0
            for y in range(self.h):
                black_count += self.field[y].count("#")
            ans = self.h * self.w - black_count - min_dis - 1
            print(ans)


Solver().solve()
