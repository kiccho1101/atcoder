S = input()
T = input()

N = len(S)
M = len(T)

INF = 10 ** 18
# dp[i][j]: Sのi文字目まででTのj文字目までに変換する最小の手数
dp = [[INF] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
    for j in range(M):
        # 変更
        if S[i] == T[j]:
            dp[i + 1][j + 1] = dp[i][j]
        else:
            dp[i + 1][j + 1] = dp[i][j] + 1

        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i + 1][j] + 1, dp[i][j + 1] + 1)

print(dp[N][M])
