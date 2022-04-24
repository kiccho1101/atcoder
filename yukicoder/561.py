N, D = map(int, input().split())
tk = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i日目に東京か京都にいるときの収入の最大値
dp = [[0] * 2 for _ in range(N + 1)]

dp[0][0] = 0
dp[0][1] = -D
for i in range(N):
    t, k = tk[i]
    dp[i + 1][0] = max(dp[i][0] + t, dp[i][1] - D + k)
    dp[i + 1][1] = max(dp[i][1] + k, dp[i][0] - D + t)

print(max(dp[N][0], dp[N][1]))
