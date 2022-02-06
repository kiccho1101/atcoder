N, M = map(int, input().split())
field = [list(input()) for _ in range(N)]


def dfs(x, y):
    field[x][y] = "."

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == "W":
                dfs(nx, ny)
    return


import numpy as np

ans = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == "W":
            dfs(i, j)
            ans += 1
print(ans)
