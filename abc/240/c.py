N, X = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(N)]

dp = [[False] * (X + 1) for _ in range(N + 1)]

dp[0][0] = True
for i in range(N):
    a, b = ab[i]
    for j in range(X + 1):
        if j + a <= X:
            dp[i + 1][j + a] |= dp[i][j]
        if j + b <= X:
            dp[i + 1][j + b] |= dp[i][j]

if dp[N][X]:
    print("Yes")
else:
    print("No")
