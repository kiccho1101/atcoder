W = int(input())
N, K = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]

# dp[k][j]: i枚目まででk枚を使って幅jになる重要度の最大値
dp = [[0] * (W + 1) for _ in range(K + 1)]
ans = 0
for a, b in ab:
    ndp = [[0] * (W + 1) for _ in range(K + 1)]
    for k in range(1, K + 1):
        for j in range(W + 1):
            ndp[k][j] = dp[k][j]
            if j - a >= 0:
                ndp[k][j] = max(dp[k][j], dp[k - 1][j - a] + b)
            ans = max(ans, ndp[k][j])

    dp = ndp

print(ans)
