_ = input()

S = input()

MOD = 10 ** 9 + 7
dp = [0] * 7
for s in S:
    if s == "a":
        dp[0] += 1
    elif s == "t":
        dp[1] += dp[0]
    elif s == "c":
        dp[2] += dp[1]
    elif s == "o":
        dp[3] += dp[2]
    elif s == "d":
        dp[4] += dp[3]
    elif s == "e":
        dp[5] += dp[4]
    elif s == "r":
        dp[6] += dp[5]
    if s in "atcoder":
        print(s, dp)
print(dp[-1] % MOD)
