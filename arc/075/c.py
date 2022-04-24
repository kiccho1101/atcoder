N = int(input())
s = [int(input()) for _ in range(N)]

M = 10000
# dp[i][j]: i問目までで得点がjになるかどうか
dp = [[False] * (M + 1) for _ in range(N + 1)]

dp[0][0] = True
for i in range(N):
    for j in range(M + 1):
        dp[i + 1][j] |= dp[i][j]
        if j - s[i] >= 0:
            dp[i + 1][j] |= dp[i][j - s[i]]

for i in reversed(range(M + 1)):
    if dp[N][i] and i % 10 != 0:
        print(i)
        exit()

print(0)
