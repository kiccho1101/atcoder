h, w = map(int, input().split())
Q = int(input())
qs = [list(map(int, input().split())) for _ in range(Q)]

par = [i for i in range(h * w + 2)]
field = [[0] * (w + 2) for _ in range(h + 2)]
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y
    return


for q in qs:
    if q[0] == 1:
        ay, ax = q[1], q[2]
        field[ay][ax] = 1
        for dy, dx in ds:
            ny, nx = ay + dy, ax + dx
            if field[ny][nx] == 1:
                unite((ay - 1) * w + ax, (ny - 1) * w + nx)
    elif q[0] == 2:
        ay, ax, by, bx = q[1], q[2], q[3], q[4]
        if same((ay - 1) * w + ax, (by - 1) * w + bx) and field[ay][ax] == 1 and field[by][bx] == 1:
            print("Yes")
        else:
            print("No")
