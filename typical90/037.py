W, N = map(int, input().split())

dp = [-1 for _ in range(W + 1)]
dp[0] = 0

for i in range(N):
    l, r, v = map(int, input().split())

    for j in reversed(range(W)):
        if dp[j] != -1:
            if j + l <= W:
                dp[j + l] = max(dp[j] + v, dp[j + l])
                if j + r < W:
                    dp[j + r] = max(dp[j] + v, dp[j + r])
                elif W <= j + r:
                    dp[W] = max(dp[j] + v, dp[W])

print(dp[W])
