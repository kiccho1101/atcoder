N, K = map(int, input().split())
hs = list(map(int, input().split()))

INF = 10 ** 18
dp = [INF] * N
dp[0] = 0
for i in range(1, N):
    for j in range(1, K + 1):
        if i - j > -1:
            dp[i] = min(dp[i], dp[i - j] + abs(hs[i] - hs[i - j]))

print(dp[N - 1])
