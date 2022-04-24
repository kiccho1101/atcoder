N = int(input())

ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

if N == ng1 or N == ng2 or N == ng3:
    print("NO")
    exit()

# dp[i][j]: i回目の操作でjになれるかどうか
dp = [[False] * (N + 5) for _ in range(101)]

dp[0][N] = True
for i in range(100):
    for j in range(N + 1):
        if j not in [ng1, ng2, ng3]:
            dp[i + 1][j] |= dp[i][j]
            dp[i + 1][j] |= dp[i][j + 1]
            dp[i + 1][j] |= dp[i][j + 2]
            dp[i + 1][j] |= dp[i][j + 3]


if dp[100][0]:
    print("YES")
else:
    print("NO")
