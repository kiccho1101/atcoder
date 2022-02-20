import sys
sys.setrecursionlimit(10 ** 6)
N, X = map(int, input().split())

A = [list(map(int, input().split()))[1:] for _ in range(N)]

ans = 0


def dfs(pos, prod):
    global ans
    if pos == N:
        if prod == X:
            ans += 1
        return

    for a in A[pos]:
        if X % a != 0 or a * prod > X:
            continue
        dfs(pos + 1, a * prod)


dfs(0, 1)

print(ans)
