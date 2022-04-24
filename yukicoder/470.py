N = int(input())
A = list(map(int, input().split()))

M = 1 << 15

# dp[i][j]:  i番目までの数字でjにできるかどうか
dp = [False] * (M + 1)
dp[0] = True
for i in range(N):
    ndp = [False] * (M + 1)
    for j in range(M + 1):
        ndp[j] = dp[j]
        if j ^ A[i] < M + 1:
            ndp[j] |= dp[j ^ A[i]]
    dp = ndp

print(sum(dp))
