import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

size = [0] * (N)


def dfs(x, past=-1):
    size[x] += 1
    for to in edge[x]:
        if to == past:
            continue
        dfs(to, x)
        size[x] += size[to]


dfs(0)

ans = 0
for i in range(N):
    ans += size[i] * (N - size[i])

print(ans)
