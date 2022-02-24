N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]


V = 10 ** 5 + 10
INF = 10 ** 18

# dp[i][j]: i番目の商品まで選んで価値がjになる重さの最小値
dp = [[INF] * (V + 1) for _ in range(N + 1)]

dp[0][0] = 0
ans = 0
for i in range(1, N + 1):
    w, v = items[i - 1]
    for j in range(0, V + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        if j - v > -1:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v] + w)

        if dp[i][j] <= W:
            ans = max(ans, j)

print(ans)
