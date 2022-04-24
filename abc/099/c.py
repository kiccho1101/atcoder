N = int(input())

INF = 10 ** 18

# dp[i]: i円引き出すのに必要な最小の操作回数
dp = [INF] * (N + 1)

dp[0] = 0
for i in range(N + 1):
    # 1円
    if i - 1 >= 0 and dp[i - 1] != INF:
        dp[i] = min(dp[i], dp[i - 1] + 1)

    # 6円
    j = 1
    while i - pow(6, j) >= 0:
        if dp[i - pow(6, j)] != INF:
            dp[i] = min(dp[i], dp[i - pow(6, j)] + 1)
        j += 1

    # 9円
    j = 1
    while i - pow(9, j) >= 0:
        if dp[i - pow(9, j)] != INF:
            dp[i] = min(dp[i], dp[i - pow(9, j)] + 1)
        j += 1

print(dp[N])
