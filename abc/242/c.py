MOD = 998244353
N = int(input())

# dp[i][j]: i桁で、i桁目がjである数の通り数
dp = [[0] * 10 for _ in range(N + 1)]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, N + 1):
    for j in range(1, 10):
        if j == 1:
            dp[i][j] += dp[i - 1][j] + dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j]
        else:
            dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        dp[i][j] %= MOD

print(sum(dp[N]) % MOD)
