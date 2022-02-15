N, L = map(int, input().split())
MOD = 10 ** 9 + 7

dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    if i - L >= 0:
        dp[i] += dp[i - L]
    dp[i] %= MOD

print(dp[-1])
