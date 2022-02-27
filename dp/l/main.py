N = int(input())

A = list(map(int, input().split()))

# dp[i][j]: [i, j)が残ってる状態から始めたときの最終的なX-Yの値
dp = [[0] * (N + 2) for _ in range(N + 2)]

for i in range(N):
    for j in range(1, N + 1):
        if i + j <= N:
            dp[i + 1][j] = max(A[j - 1] - dp[i][j + 1], A[i + j - 1] - dp[i][j])

print(dp[N][1])
