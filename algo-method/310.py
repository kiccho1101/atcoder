N, M = map(int, input().split())
A = list(map(int, input().split()))

MOD = 1000

# dp[i][j]: i番目までの数字で和がjになる通り数
dp = [[0] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(M + 1):
        dp[i][j] += dp[i - 1][j]
        if j - A[i - 1] >= 0:
            dp[i][j] += dp[i - 1][j - A[i - 1]]

print(dp[N][M])
