N, Ma, Mb = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10 ** 18
# dp[i][j][k]: i番目までの薬品でタイプAをjグラム、タイプBをkグラム買うのに必要な最小の予算
dp = [[[INF] * 401 for _ in range(401)] for _ in range(N + 1)]

dp[0][0][0] = 0
for i in range(N):
    a, b, c = abc[i]
    for j in range(401):
        for k in range(401):
            dp[i + 1][j][k] = dp[i][j][k]
            if j - a >= 0 and k - b >= 0:
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j - a][k - b] + c)

ans = INF
for j in range(1, 401):
    for k in range(1, 401):
        if j / k == Ma / Mb:
            ans = min(ans, dp[N][j][k])

if ans == INF:
    print(-1)
else:
    print(ans)
