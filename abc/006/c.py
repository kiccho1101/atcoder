N, M = map(int, input().split())

for a in range(0, N + 1):
    b = -2 * a - M + 4 * N
    c = N - a - b
    if b >= 0 and c >= 0:
        print(a, b, c)
        exit()

print(-1, -1, -1)
