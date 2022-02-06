import numpy as np

N = input()
S = input()

MOD = 10 ** 9 + 7
dp = [[0 for _ in range(7)] for _ in range(len(S) + 1)]
for i, s in enumerate(S):
    dp[i + 1] = dp[i].copy()
    if s == "a":
        dp[i + 1][0] += 1
    elif s == "t":
        dp[i + 1][1] += dp[i][0]
    elif s == "c":
        dp[i + 1][2] += dp[i][1]
    elif s == "o":
        dp[i + 1][3] += dp[i][2]
    elif s == "d":
        dp[i + 1][4] += dp[i][3]
    elif s == "e":
        dp[i + 1][5] += dp[i][4]
    elif s == "r":
        dp[i + 1][6] += dp[i][5]
print(np.array(dp))
