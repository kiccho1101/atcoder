N = int(input())

H = 1000
W = 1000

cum = [[0] * (W + 1) for _ in range(H + 1)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        cum[ly][x] += 1
        cum[ry][x] -= 1

for x in range(W + 1):
    for y in range(H - 1):
        cum[y + 1][x] += cum[y][x]

ans = [0] * N
for x in range(W + 1):
    for y in range(H + 1):
        if cum[y][x] > 0:
            ans[cum[y][x] - 1] += 1

print(*ans, sep="\n")
