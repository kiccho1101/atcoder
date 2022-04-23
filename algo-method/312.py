N, M, K = map(int, input().split())
A = list(map(int, input().split()))

INF = 10 ** 18
# dp[i][j]: i番目までの数字で総和がjになる最小の整数の数
dp = [[INF] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        dp[i + 1][j] = dp[i][j]
        if j - A[i] >= 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - A[i]] + 1)

if dp[N][M] <= K:
    print("Yes")
else:
    print("No")
