N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i番目の品物までで、重さjになる価値の最大値
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        w, v = items[i]
        dp[i + 1][j] = dp[i][j]
        if j - w >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)

print(dp[N][W])
