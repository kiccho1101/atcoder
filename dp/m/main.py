N, K = map(int, input().split())

A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

# dp[i][j]: i番目の子供までにj個のアメちゃんを配る通り数
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp_sum = [[1] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    a = A[i - 1]
    for j in range(K + 1):
        dp[i][j] = dp_sum[i - 1][j]
        if j - a - 1 >= 0:
            dp[i][j] -= dp_sum[i - 1][j - a - 1]

        if j - 1 >= 0:
            dp_sum[i][j] = dp_sum[i][j - 1] + dp[i][j]
        else:
            dp_sum[i][j] = dp_sum[i][j]

        dp[i][j] %= MOD
        dp_sum[i][j] %= MOD

print(dp[N][K])
