INF = 10 ** 18

T = int(input())

cases = [list(map(int, input().split())) for _ in range(T)]

for a in cases:
    a.sort()
    x, y, z = a
    b = INF
    if (y - x) % 3 == 0:
        b = min(b, y)
    if (z - x) % 3 == 0 or (z - y) % 3 == 0:
        b = min(b, z)
    if b == INF:
        b = -1
    print(b)
