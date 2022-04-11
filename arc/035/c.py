INF = 10 ** 18
N, M = map(int, input().split())
mat = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    mat[a][b] = t
    mat[b][a] = t


K = int(input())
xyz = [list(map(int, input().split())) for _ in range(K)]

for i in range(N):
    mat[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])


for x, y, z in xyz:
    x -= 1
    y -= 1
    mat[x][y] = min(mat[x][y], z)
    mat[y][x] = min(mat[y][x], z)
    for k in [x, y]:
        for i in range(N):
            for j in range(N):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
    S = sum([sum(row) for row in mat]) // 2
    print(S)
