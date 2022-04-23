N, M = map(int, input().split())

ab = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10 ** 18

# dp[i][j]: i番目までの数字で和がjとするときのA[i]の個数の最小値
dp = [[INF] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
    a, b = ab[i]
    for j in range(M + 1):
        dp[i + 1][j] = dp[i][j]
        if j - a >= 0:
            if dp[i][j - a] < INF:
                dp[i + 1][j] = min(dp[i + 1][j], 1)
            if dp[i + 1][j - a] < b:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - a] + 1)

if dp[N][M] < INF:
    print("Yes")
else:
    print("No")
