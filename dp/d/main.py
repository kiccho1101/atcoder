N, W = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dp = [[0] * (W + 1) for _ in range(N)]
for i in range(N):
    w, v = items[i]
    if i == 0:
        dp[i][w] = v
        ans = max(ans, dp[i][w])
    else:
        for j in range(1, W + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j - w > -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
            ans = max(ans, dp[i][j])

print(ans)
