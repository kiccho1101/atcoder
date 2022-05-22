def solve(S):
    L = len(S)

    # dp[i][j][k]: i桁目まででj(N未満か)でk(4または9か)の数字が出現する回数
    dp = [[[0] * 2 for _ in range(2)] for _ in range(L + 1)]
    dp[0][0][0] = 1
    for i in range(L):
        D = int(S[i])
        for j in range(2):
            for k in range(2):
                for d in range(10 if j == 1 else D + 1):
                    dp[i + 1][int(j or d < D)][int(k or d == 4 or d == 9)] += dp[i][j][
                        k
                    ]

    return dp[L][0][1] + dp[L][1][1]


A, B = map(int, input().split())
a = solve(str(A - 1))
b = solve(str(B))
print(b - a)
