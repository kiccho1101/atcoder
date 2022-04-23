N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = 10 ** 18
# dp[i][j]: i個まで使って総和をjにする個数の最小値
dp = [[INF] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(M + 1):
        dp[i][j] = dp[i - 1][j]
        if j - A[i - 1] >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - A[i - 1]] + 1)

if dp[N][M] == INF:
    print(-1)
else:
    print(dp[N][M])
