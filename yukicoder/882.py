N = int(input())

# dp[i][j]: 長さiで最後がj(ケン/パ)の通り数
# j = 0: パ
# j = 1: ケン
# j = 2: ケンケン
dp = [[0] * 3 for _ in range(N + 1)]

MOD = 10 ** 9 + 7
dp[0][0] = 1
for i in range(N):
    dp[i + 1][0] += dp[i][1] + dp[i][2]
    dp[i + 1][0] %= MOD

    dp[i + 1][1] += dp[i][0]
    dp[i + 1][1] %= MOD

    dp[i + 1][2] += dp[i][1]
    dp[i + 1][2] %= MOD


print(sum(dp[N]) % MOD)
