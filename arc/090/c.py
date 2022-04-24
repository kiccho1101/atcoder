N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i][j] : i列目まででj行目にいるときに回収できるあめの個数の最大値
dp = [[0] * 2 for _ in range(N + 1)]

for i in range(N):
    dp[i + 1][0] = dp[i][0] + A[i]
    dp[i + 1][1] = max(dp[i][1] + B[i], dp[i + 1][0] + B[i])

print(max(dp[N][0], dp[N][1]))
