N = int(input())
A = list(map(int, input().split()))

INF = 10 ** 18

# dp[i][j]: i番目までの金でi番目を選んだときと選んでないときの最小値
dp1 = [[INF, INF] for _ in range(N)]
dp2 = [[INF, INF] for _ in range(N)]

ans = INF

# 0番目を選んだ時 -> N-1番目は選んでも選ばなくても良い
dp1[0][1] = A[0]
for i in range(1, N):
    dp1[i][0] = dp1[i - 1][1]
    dp1[i][1] = min(dp1[i - 1][0] + A[i], dp1[i - 1][1] + A[i])

# 0番目を選ばない時 -> N-1番目は選ぶ必要がある
dp2[0][0] = 0
for i in range(1, N):
    if i < N - 1:
        dp2[i][0] = dp2[i - 1][1]
    dp2[i][1] = min(dp2[i - 1][0] + A[i], dp2[i - 1][1] + A[i])

ans = min(min(dp1[N - 1]), min(dp2[N - 1]))
print(ans)
