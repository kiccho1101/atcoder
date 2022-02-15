N = int(input())

MOD = 10 ** 9 + 7
A = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N
dp[0] = sum(A[0])
for i in range(1, N):
    dp[i] = dp[i - 1] * sum(A[i])
    dp[i] %= MOD

print(dp[-1])
