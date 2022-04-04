from collections import deque


H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
INF = 10 ** 18


class Solver:
    def __init__(self):
        self.ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(self, y, x):
        dists = [[INF] * W for _ in range(H)]
        dists[y][x] = 0
        queue = deque([(y, x)])
        vis = [[False] * W for _ in range(H)]
        while queue:
            y, x = queue.popleft()
            if vis[y][x]:
                continue
            vis[y][x] = True
            for dy, dx in self.ds:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W and field[ny][nx] != "#":
                    dists[ny][nx] = dists[y][x] + 1
                    queue.append((ny, nx))

        max_dist = 0
        for y in range(H):
            for x in range(W):
                if dists[y][x] != INF:
                    max_dist = max(max_dist, dists[y][x])
        return max_dist - 1

    def solve(self):
        ans = 0
        for y in range(H):
            for x in range(W):
                if field[y][x] != "#":
                    ans = max(ans, self.bfs(y, x))

        print(ans)


Solver().solve()
