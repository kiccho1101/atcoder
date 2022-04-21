N, M = map(int, input().split())
A = list(map(int, input().split()))


# dp[i][j]: i番目までの整数で和がjになるかどうか
dp = [[False] * (M + 1) for _ in range(N + 1)]


dp[0][0] = True
for i in range(1, N + 1):
    for j in range(M + 1):
        dp[i][j] = dp[i - 1][j]
        if j - A[i - 1] >= 0:
            dp[i][j] |= dp[i - 1][j - A[i - 1]]

if dp[N][M]:
    print("Yes")
else:
    print("No")
