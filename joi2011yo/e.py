from collections import deque

INF = 10 ** 18


class Mouse:
    def __init__(self):
        self.h, self.w, self.n = map(int, input().split())
        self.field = [list(input()) for _ in range(self.h)]
        self.cheese = {}
        for y in range(self.h):
            for x in range(self.w):
                if self.field[y][x] == "S":
                    self.cheese[0] = (y, x)
                elif self.field[y][x].isdigit():
                    self.cheese[int(self.field[y][x])] = (y, x)
        self.ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bfs(self, start, goal):
        dist = [[INF] * self.w for _ in range(self.h)]
        dist[start[0]][start[1]] = 0
        queue = deque([])
        queue.append(start)
        vis = [[False] * self.w for _ in range(self.h)]
        while queue:
            y, x = queue.popleft()
            if (y, x) == goal:
                continue
            if vis[y][x]:
                continue
            vis[y][x] = True
            for dy, dx in self.ds:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < self.h and 0 <= nx < self.w and self.field[ny][nx] != "X":
                    dist[ny][nx] = min(dist[ny][nx], dist[y][x] + 1)
                    queue.append((ny, nx))
        return dist[goal[0]][goal[1]]

    def solve(self):
        ans = 0
        for i in range(self.n):
            ans += self.bfs(self.cheese[i], self.cheese[i + 1])
        print(ans)


Mouse().solve()
