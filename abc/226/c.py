import sys

sys.setrecursionlimit(2 * 10 ** 5)

N = int(input())

ts = []
A = []
needed = set()

for _ in range(N):
    i = list(map(int, input().split()))
    ts.append(i[0])
    A.append([_i - 1 for _i in i[2:]])


def dfs(x):
    for a in A[x]:
        if a in needed:
            continue
        needed.add(a)
        dfs(a)


needed.add(N - 1)
dfs(N - 1)

ans = 0
for i in needed:
    ans += ts[i]
print(ans)
