N = int(input())
W = list(map(int, input().split()))

# dp[i][j]: i番目までのおもりで左がjになるかどうか
dp = [[False] * 10001 for _ in range(N + 1)]

dp[0][0] = True
for i in range(N):
    for j in range(10001):
        w = W[i]
        dp[i + 1][j] = dp[i][j]
        if j - w >= 0:
            dp[i + 1][j] |= dp[i][j - w]

s = sum(W)
if s % 2 == 1 or not dp[N][s // 2]:
    print("impossible")
else:
    print("possible")
