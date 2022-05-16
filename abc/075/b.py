H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
ans = [[0] * W for _ in range(H)]

ds = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

for y in range(H):
    for x in range(W):
        if field[y][x] == "#":
            ans[y][x] = -1

            for dy, dx in ds:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W and ans[ny][nx] != -1:
                    ans[ny][nx] += 1


for y in range(H):
    print("".join([str(ans[y][x]) if ans[y][x] != -1 else "#" for x in range(W)]))
