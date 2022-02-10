N, _ = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

mat_T = list(zip(*mat))

for row in mat_T:
    print(*row)
