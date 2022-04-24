N = int(input())

# dp[i]: i番目のマスに行く方法のパターン数
dp = [0] * (N + 1)

dp[0] = 1
for i in range(N):
    dp[i + 1] += dp[i]
    if i - 1 >= 0:
        dp[i + 1] += dp[i - 1]
print(dp[N])
