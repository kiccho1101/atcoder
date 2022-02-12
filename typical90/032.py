# %%
from itertools import permutations

N = int(input())

v = [[0] * N for _ in range(N)]
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        v[i][j] = a[j]

M = int(input())
ng = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ng[a][b] = True
    ng[b][a] = True

INF = 10 ** 18
ans = INF
for p in permutations(range(N)):
    flag = True
    for i in range(N - 1):
        if ng[p[i]][p[i + 1]]:
            flag = False
            break
    if not flag:
        continue

    t = 0
    for i in range(N):
        t += v[p[i]][i]
    ans = min(ans, t)

if ans == INF:
    print(-1)
else:
    print(ans)
