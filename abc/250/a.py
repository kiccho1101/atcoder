H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for dx, dy in ds:
    nx = R + dx
    ny = C + dy
    if 1 <= nx <= H and 1 <= ny <= W:
        ans += 1

print(ans)
