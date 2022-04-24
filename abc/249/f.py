import numpy


N, K = map(int, input().split())
ty = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    if ty[i][0] == 2 and ty[i - 1][0] == 2:
        ty[i][1] = ty[i - 1][1] + ty[i][1]

print(numpy.array(ty))
