H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for y in range(H):
    for x in range(W):
        if field[y][x] == "#":
            flag = False
            for dy, dx in ds:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W and field[ny][nx] == "#":
                    flag = True
            if not flag:
                print("No")
                exit()

print("Yes")
