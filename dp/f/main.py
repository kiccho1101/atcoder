S = input()
T = input()

S_n = len(S)
T_n = len(T)

# dp[i][j]: Sのi番目までの文字列とTのj番目までの文字列のLCS
dp = [[0] * (T_n + 1) for _ in range(S_n + 1)]
dp_s = [[""] * (T_n + 1) for _ in range(S_n + 1)]

for i in range(1, S_n + 1):
    s = S[i - 1]
    for j in range(1, T_n + 1):
        t = T[j - 1]
        if dp[i][j - 1] < dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j]
            dp_s[i][j] = dp_s[i - 1][j]
        else:
            dp[i][j] = dp[i][j - 1]
            dp_s[i][j] = dp_s[i][j - 1]
        if s == t:
            if dp[i][j] < dp[i - 1][j - 1] + 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                dp_s[i][j] = dp_s[i - 1][j - 1] + s

print(dp_s[S_n][T_n])
