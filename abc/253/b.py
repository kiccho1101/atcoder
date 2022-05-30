import heapq


H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]


sy, sx = -1, -1
ey, ex = -1, -1
for y in range(H):
    for x in range(W):
        if field[y][x] == "o":
            if sy == -1:
                sy, sx = y, x
            elif ey == -1:
                ey, ex = y, x
            else:
                break

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = [(0, sy, sx)]
INF = 10 ** 18
dist = [[INF] * W for _ in range(H)]
dist[sy][sx] = 0
while queue:
    d, y, x = heapq.heappop(queue)
    for dy, dx in ds:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < H and 0 <= nx < W:
            if dist[y][x] != INF and dist[ny][nx] > d + 1:
                dist[ny][nx] = d + 1
                heapq.heappush(queue, (d + 1, ny, nx))

print(dist[ey][ex])
