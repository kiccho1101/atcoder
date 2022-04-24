N, M = map(int, input().split())

not_allowed = set()
for _ in range(M):
    a = int(input())
    not_allowed.add(a)

# dp[i]: i段目に行く通り数
dp = [0] * (N + 1)

MOD = 10 ** 9 + 7

dp[0] = 1
for i in range(N):
    if i not in not_allowed:
        dp[i + 1] += dp[i]
        dp[i + 1] %= MOD
    if i - 1 >= 0 and i - 1 not in not_allowed:
        dp[i + 1] += dp[i - 1]
        dp[i + 1] %= MOD

print(dp[N] % MOD)
