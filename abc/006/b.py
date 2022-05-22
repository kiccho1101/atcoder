n = int(input())
dp = [0] * (n + 5)

MOD = 10007

dp[0] = 0
dp[1] = 0
dp[2] = 0
dp[3] = 1

if n <= 3:
    print(dp[n])
    exit()

for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    dp[i] %= MOD

print(dp[n])
