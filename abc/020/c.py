from collections import deque
import heapq


H, W, T = map(int, input().split())
field = [list(input()) for _ in range(H)]

sx, sy = -1, -1
gx, gy = -1, -1
for y in range(H):
    for x in range(W):
        if field[y][x] == "S":
            sx, sy = x, y
        elif field[y][x] == "G":
            gx, gy = x, y


ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

INF = 10 ** 18


def ok(mid, field):
    dist = [[INF] * W for _ in range(H)]
    dist[sy][sx] = 0
    queue = []
    heapq.heappush(queue, (0, sy, sx))
    while queue:
        d, y, x = heapq.heappop(queue)
        for dy, dx in ds:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and dist[y][x] != INF:
                c = mid if field[ny][nx] == "#" else 1
                if dist[ny][nx] > dist[y][x] + c:
                    dist[ny][nx] = dist[y][x] + c
                    heapq.heappush(queue, (dist[ny][nx], ny, nx))
    return dist[gy][gx] <= T


left = -1
right = 10 ** 9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if ok(mid, field):
        left = mid
    else:
        right = mid

print(left)
