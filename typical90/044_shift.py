N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift = 0

qs = [list(map(int, input().split())) for _ in range(Q)]

for [t, x, y] in qs:
    x, y = x - 1, y - 1
    if t == 1:
        x_idx = (x - shift) % N
        y_idx = (y - shift) % N
        A[x_idx], A[y_idx] = A[y_idx], A[x_idx]

    if t == 2:
        shift += 1

    if t == 3:
        x_idx = (x - shift) % N
        print(A[x_idx])
