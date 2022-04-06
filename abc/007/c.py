from collections import deque


R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
field = [list(input()) for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

INF = 10 ** 18

dist = 0
ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
queue = deque()
queue.append((sy, sx, dist))
ans = INF
vis = set()
while queue:
    y, x, d = queue.popleft()
    if (y, x) in vis:
        continue
    vis.add((y, x))
    for dy, dx in ds:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C and field[ny][nx] != "#":
            if ny == gy and nx == gx:
                ans = min(ans, d + 1)
            else:
                queue.append((ny, nx, d + 1))

print(ans)
