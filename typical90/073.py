import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
C = list(map(lambda c: 1 if c == "a" else 0, input().split()))
MOD = 10 ** 9 + 7

edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda n: int(n) - 1, input().split())
    edge[a].append(b)
    edge[b].append(a)

dp = [[0] * 3 for _ in range(N)]


def dfs(now, last=-1):
    dp[now][C[now]] = 1
    dp[now][2] = 1
    for to in edge[now]:
        if to == last:
            continue
        dfs(to, now)

        # どちらか一方の頂点しか含まない場合 (j = 0, 1)
        for i in (0, 1):
            # 削除しない場合
            res = dp[to][i]
            # 削除する場合
            res += dp[to][2]
            dp[now][i] *= res
            dp[now][i] %= MOD

        # 両方の文字を含む場合 (j = 2)
        dp[now][2] *= sum(dp[to]) + dp[to][2]
        dp[now][2] %= MOD

    dp[now][2] -= dp[now][C[now]]
    dp[now][2] %= MOD
    return dp[now][2]


print(dfs(0))
