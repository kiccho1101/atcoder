N, K = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]: [i, j)が残っている状態から初めてた最終的なX-Yの値
dp = [[0] * (N + 1) for _ in range(N + 1)]
