N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(W + 1):
        w, v = items[i - 1]
        dp[i][j] = dp[i - 1][j]
        if j - w >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

print(dp[N][W])
