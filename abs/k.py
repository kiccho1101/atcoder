N = int(input())

ts = [0]
xs = [0]
ys = [0]

for _ in range(N):
    t, x, y = list(map(int, input().split()))
    ts.append(t)
    xs.append(x)
    ys.append(y)

flag = False
for i in range(N):
    T = ts[i + 1] - ts[i]

    X = xs[i + 1] - xs[i]
    Y = ys[i + 1] - ys[i]

    is_within_area = Y <= -X + T and Y <= X + T and Y >= -X - T and Y >= X - T
    is_on_grid = T % 2 == (X + Y) % 2

    if is_within_area and is_on_grid:
        flag = True
    else:
        flag = False
        break

print("Yes" if flag else "No")
