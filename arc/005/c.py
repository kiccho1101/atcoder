import heapq

INF = 10 ** 18


class Solver:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.field = [list(input()) for _ in range(self.h)]
        self.ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def get_start(self):
        sy, sx, gy, gx = -1, -1, -1, -1
        for y in range(self.h):
            for x in range(self.w):
                if self.field[y][x] == "s":
                    sy, sx = y, x
                if self.field[y][x] == "g":
                    gy, gx = y, x
        return sy, sx, gy, gx

    def bfs(self):
        sy, sx, gy, gx = self.get_start()
        assert sy != -1 and sx != -1 and gy != -1 and gx != -1

        queue = []
        heapq.heappush(queue, (0, sy, sx, 2))
        dist = [[[INF] * 3] for _ in range(self.w) for _ in range(self.h)]
        dist[sy][sx][2] = 0
        while queue:
            d, y, x, cnt = heapq.heappop(queue)
            if y == gy and x == gx:
                break
            for dy, dx in self.ds:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < self.h and 0 <= nx < self.w:
                    if (
                        self.field[ny][nx] == "."
                        and dist[ny][nx][cnt] > dist[y][x][cnt] + 1
                    ):
                        dist[ny][nx][cnt] = dist[y][x][cnt] + 1
                        heapq.heappush(queue, (dist[ny][nx][cnt], ny, nx, cnt))
                    if (
                        self.field[ny][nx] == "#"
                        and cnt >= 1
                        and dist[ny][nx][cnt - 1] > dist[y][x][cnt] + 1
                    ):
                        dist[ny][nx][cnt - 1] = dist[y][x][cnt] + 1
                        heapq.heappush(queue, (dist[ny][nx][cnt - 1], ny, nx, cnt - 1))

        if dist[gy][gx][2] != INF and dist[gy][gx][1] != INF and dist[gy][gx][0] != INF:
            print("YES")
        else:
            print("NO")


Solver().bfs()
