N, M = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 18
# dp[i][j]: aiとbiまでを使ってできるコストの最小値
dp = [[INF] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
    for j in range(M):
        dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + cost[i][j]

print(dp[N][M])
