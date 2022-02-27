H, W = map(int, input().split())

field = [list(input()) for _ in range(H)]

MOD = 10 ** 9 + 7

# dp[i][j]: (1, 1)から(i, j)に行くやり方の数
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if field[i][j] == "#":
            dp[i][j] = 0
            continue
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]
        dp[i][j] %= MOD

print(dp[H - 1][W - 1])
