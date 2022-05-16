N, M = map(int, input().split())

students = [tuple(map(int, input().split())) for _ in range(N)]
points = [tuple(map(int, input().split())) for _ in range(M)]

INF = 10 ** 18
ans = [-1] * N
for si in range(N):
    min_d = INF
    min_pi = -1
    sx, sy = students[si]
    for pi in range(M):
        px, py = points[pi]
        d = abs(sx - px) + abs(sy - py)
        if min_d > d:
            min_d = d
            min_pi = pi
    ans[si] = min_pi + 1

for si in range(N):
    print(ans[si])
