INF = 10 ** 18
N, M = map(int, input().split())

dp = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = t
    dp[b][a] = t

for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[i][k] != INF and dp[k][j] != INF:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

print(min([max(row) for row in dp]))
