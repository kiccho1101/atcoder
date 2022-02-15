import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i].sort()

ans = []


def dfs(x, past=-1):
    ans.append(x + 1)
    for nxt in graph[x]:
        if nxt != past:
            dfs(nxt, x)
            ans.append(x + 1)


dfs(0)
print(*ans)
