N = int(input())

A = list(map(int, input().split()))

# dp[i][j][k]: 3個の皿がi枚、2個の皿がj枚、1個の皿がk枚の状態から食べ終わるまでの操作回数の期待値
dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

for k in range(N + 1):
    for j in range(N - k + 1):
        for i in range(N - k - j + 1):
            cal = i + j + k
            if cal == 0:
                continue

            res = N / cal
            if i:
                res += dp[i - 1][j][k] * i / cal
            if j:
                res += dp[i + 1][j - 1][k] * j / cal
            if k:
                res += dp[i][j + 1][k - 1] * k / cal
            dp[i][j][k] = res

print(dp[A.count(1)][A.count(2)][A.count(3)])
