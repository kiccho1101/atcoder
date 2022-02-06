S = input()

mod = 10 ** 9 + 7
target = "chokudai"
dp = [[0 for _ in range(len(target) + 1)] for _ in range(len(S) + 1)]

for i, s in enumerate(S):
    dp[i + 1] = dp[i].copy()
    for j in range(len(target)):
        if s == target[j]:
            if j == 0:
                dp[i + 1][j + 1] += 1
            else:
                dp[i + 1][j + 1] += dp[i][j]

print(dp[-1][-1] % mod)
