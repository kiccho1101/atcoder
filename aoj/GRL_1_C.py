INF = 10 ** 18
V, E = map(int, input().split())
dp = [[INF] * V for _ in range(V)]
for i in range(V):
    dp[i][i] = 0
for _ in range(E):
    s, t, d = map(int, input().split())
    dp[s][t] = d

for k in range(V):
    for i in range(V):
        for j in range(V):
            if dp[i][k] != INF and dp[k][j] != INF:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(V):
    if dp[i][i] < 0:
        print("NEGATIVE CYCLE")
        exit()

for row in dp:
    print(*["INF" if v == INF else v for v in row])
