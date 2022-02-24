import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

memo = [0] * N
vis = [False] * N


def dp(x):
    if vis[x]:
        return memo[x]
    ans = 0
    for to in graph[x]:
        ans = max(ans, dp(to) + 1)
    vis[x] = True
    memo[x] = ans
    return ans


ans = 0
for i in range(N):
    ans = max(ans, dp(i))

print(ans)
