N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

MM = 500
# dp[i][j]: i番目の国まででj円にできるかどうか
dp = [[False] * (MM + 1) for _ in range(N + 1)]

dp[0][0] = True
for i in range(N):
    for j in range(MM + 1):
        for m in range(M):
            if j - A[i][m] >= 0:
                dp[i + 1][j] |= dp[i][j - A[i][m]]


for i in range(K, -1, -1):
    if dp[N][i]:
        print(K - i)
        exit()

print(-1)
