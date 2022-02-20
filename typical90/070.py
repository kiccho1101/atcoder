N = int(input())

xs = []
ys = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)


xs.sort()
ys.sort()

if N % 2 == 0:
    mid_x = ((xs[N // 2 - 1] + xs[N // 2])) // 2
    mid_y = ((ys[N // 2 - 1] + ys[N // 2])) // 2
else:
    mid_x = xs[N // 2]
    mid_y = ys[N // 2]


ans = 0
for i in range(N):
    ans += abs(xs[i] - mid_x) + abs(ys[i] - mid_y)

print(ans)
