S = input()
T = input()

N = len(S)
M = len(T)

# dp[i][j]: Sのi文字目までとTのj文字目まででのLCSの長さ
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = max(
                dp[i][j] + 1,
                dp[i + 1][j],
                dp[i][j + 1],
            )
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[N][M])
