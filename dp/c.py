N = int(input())

abc = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i日目にjをしたときの幸福度の最大値
dp = [[0] * 3 for _ in range(N + 1)]

for i in range(N):
    a, b, c = abc[i]
    dp[i + 1][0] = max(dp[i][1], dp[i][2]) + a
    dp[i + 1][1] = max(dp[i][0], dp[i][2]) + b
    dp[i + 1][2] = max(dp[i][0], dp[i][1]) + c


print(max(dp[N][0], dp[N][1], dp[N][2]))
