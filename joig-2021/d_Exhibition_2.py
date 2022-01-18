N, M, D = map(int, input().split())

xs = []
vs = []
for _ in range(N):
    x, v = map(int, input().split())
    xs.append(x)
    vs.append(v)


def check(mid, xs, vs, N, M):
    cnt = 0
    last_idx = -1
    for i in range(N):
        if vs[i] >= mid and (last_idx == -1 or xs[i] - xs[last_idx] >= D):
            cnt += 1
            last_idx = i

    return cnt >= M


s = sorted([{"v": vs[i], "x": xs[i]} for i in range(len(vs))], key=lambda d: d["x"])
xs = [d["x"] for d in s]
vs = [d["v"] for d in s]

left = min(vs) - 1
min_left = left
right = max(vs) + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if check(mid, xs, vs, N, M):
        left = mid
    else:
        right = mid

print(-1 if min_left == left else left)
