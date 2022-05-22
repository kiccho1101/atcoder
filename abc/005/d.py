import collections


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
ps = [int(input()) for _ in range(Q)]

if N > 1:
    for y in range(N):
        for x in range(1, N):
            field[y][x] += field[y][x - 1]

    for x in range(N):
        for y in range(1, N):
            field[y][x] += field[y - 1][x]


def get_sum(field, y1, x1, y2, x2):
    y1 -= 1
    x1 -= 1
    ans = field[y2][x2]
    if x1 >= 0:
        ans -= field[y2][x1]
    if y1 >= 0:
        ans -= field[y1][x2]
    if x1 >= 0 and y1 >= 0:
        ans += field[y1][x1]
    return ans


max_deli = collections.defaultdict(int)
for y1 in range(N):
    for x1 in range(N):
        for y2 in range(y1, N):
            for x2 in range(x1, N):
                deli = get_sum(field, y1, x1, y2, x2)
                dy = y2 - y1 + 1
                dx = x2 - x1 + 1
                takos = dy * dx
                max_deli[takos] = max(max_deli[takos], deli)

ans = [0] * 2501
for i in range(1, 2501):
    ans[i] = max(ans[i - 1], max_deli[i])

for p in ps:
    print(ans[p])
