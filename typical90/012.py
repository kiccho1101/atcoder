from collections import deque

H, W = map(int, input().split())

field = [["" for _ in range(W)] for _ in range(H)]

Q = int(input())
qs = [list(map(int, input().split())) for _ in range(Q)]


def check(field, q):
    ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    xa, ya, xb, yb = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
    if field[xa][ya] != "R" or field[xb][yb] != "R":
        return False
    if xa == xb and ya == yb:
        return True

    visited = set()
    q = deque()
    q.append([xa, ya])
    visited.add(str([xa, ya]))

    while q:
        xp, yp = q.popleft()
        for dx, dy in ds:
            nx, ny = xp + dx, yp + dy
            if (
                str([nx, ny]) not in visited
                and 0 <= nx < H
                and 0 <= ny < W
                and field[nx][ny] == "R"
            ):
                q.append([nx, ny])
            visited.add(str([nx, ny]))
            if nx == xb and ny == yb:
                return True

    return False


for q in qs:
    # t == 1
    if q[0] == 1:
        x, y = q[1] - 1, q[2] - 1
        field[x][y] = "R"

    # t == 2
    if q[0] == 2:
        if check(field, q):
            print("Yes")
        else:
            print("No")
