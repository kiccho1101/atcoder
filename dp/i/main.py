N = int(input())

ps = list(map(float, input().split()))

# dp[i][j]: i番目までコインを投げて(表-裏)がjになる確率
dp = [[0.0] * (2 * (N + 1)) for _ in range(N + 1)]

for i in range(1, N + 1):
    p = ps[i - 1]
    for j in range(-N, N + 1, 1):
        if i == 1:
            dp[i][1] = p
            dp[i][-1] = 1 - p
        else:
            dp[i][j] = dp[i - 1][j - 1] * p + dp[i - 1][j + 1] * (1 - p)

ans = sum(dp[N][1 : N + 1])
print(ans)
