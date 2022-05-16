H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

skip_h = set()
skip_w = set()

for y in range(H):
    flag = True
    for x in range(W):
        if field[y][x] == "#":
            flag = False
            break
    if flag:
        skip_h.add(y)

for x in range(W):
    flag = True
    for y in range(H):
        if field[y][x] == "#":
            flag = False
            break
    if flag:
        skip_w.add(x)

for y in range(H):
    if y not in skip_h:
        row = "".join([field[y][x] for x in range(W) if x not in skip_w])
        print(row)
