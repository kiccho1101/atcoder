D, G = map(int, input().split())
G //= 100
p, c = [0] * D, [0] * D

for i in range(D):
    p[i], c[i] = map(int, input().split())

c = [x // 100 for x in c]
inf = float("inf")
Max = 200000
dp = [[inf] * Max for i in range(D + 1)]
dp[0][0] = 0

for i in range(D):
    for j in range(Max):
        if not dp[i][j] == inf:
            for k in range(p[i]):
                if j + k * (i + 1) < Max:
                    dp[i + 1][j + k * (i + 1)] = min(
                        dp[i + 1][j + k * (i + 1)], dp[i][j] + k
                    )
            if j + p[i] * (i + 1) + c[i] < Max:
                dp[i + 1][j + p[i] * (i + 1) + c[i]] = min(
                    dp[i + 1][j + p[i] * (i + 1) + c[i]], dp[i][j] + p[i]
                )

# print(dp)
print(min(dp[D][G:]))
