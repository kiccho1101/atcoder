N = int(input())
hs = list(map(int, input().split()))

INF = 10 ** 18
dp = [INF] * N

dp[0] = 0
for i in range(1, N):
    if i == 1:
        dp[i] = dp[i - 1] + abs(hs[i] - hs[i - 1])
    else:
        dp[i] = min(
            dp[i - 1] + abs(hs[i] - hs[i - 1]), dp[i - 2] + abs(hs[i] - hs[i - 2])
        )

print(dp[N - 1])
