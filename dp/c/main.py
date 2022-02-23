N = int(input())

hs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
for i in range(N):
    for j in range(3):
        if i == 0:
            dp[i][j] = hs[i][j]
        else:
            for k in range(3):
                if k != j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + hs[i][j])

ans = 0
for j in range(3):
    ans = max(ans, dp[N - 1][j])

print(ans)
