import sys

sys.setrecursionlimit(10 ** 6)

N, X = map(int, input().split())
X -= 1
A = list(map(int, input().split()))

known = [False] * N


def dfs(x):
    if known[x]:
        return
    known[x] = True
    dfs(A[x] - 1)


dfs(X)
print(sum(known))
