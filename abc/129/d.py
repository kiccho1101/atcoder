H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

l_r = [[0] * W for _ in range(H)]
r_l = [[0] * W for _ in range(H)]
t_b = [[0] * W for _ in range(H)]
b_t = [[0] * W for _ in range(H)]

# l_r
for y in range(H):
    s = 0
    for x in range(W):
        if field[y][x] == "#":
            s = -1
        s += 1
        l_r[y][x] = s

# r_l
for y in range(H):
    s = 0
    for x in reversed(range(W)):
        if field[y][x] == "#":
            s = -1
        s += 1
        r_l[y][x] = s

# t_b
for x in range(W):
    s = 0
    for y in range(H):
        if field[y][x] == "#":
            s = -1
        s += 1
        t_b[y][x] = s

# b_t
for x in range(W):
    s = 0
    for y in reversed(range(H)):
        if field[y][x] == "#":
            s = -1
        s += 1
        b_t[y][x] = s


ans = 0
for y in range(H):
    for x in range(W):
        s = l_r[y][x] + r_l[y][x] + t_b[y][x] + b_t[y][x]
        s -= 3
        ans = max(ans, s)

print(ans)
