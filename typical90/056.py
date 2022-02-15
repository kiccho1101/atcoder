N, S = map(int, input().split())

A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(1, S + 1):
        if j - A[i] >= 0 and dp[i][j - A[i]]:
            dp[i + 1][j] = True
        if j - B[i] >= 0 and dp[i][j - B[i]]:
            dp[i + 1][j] = True

if not dp[N][S]:
    exit(print("Impossible"))

ans = ""
for i in reversed(range(N)):
    Bool = True
    if S - A[i] >= 0:
        if dp[i][S - A[i]]:
            ans += "A"
            S -= A[i]
            Bool = False
    if S - B[i] >= 0 and Bool:
        if dp[i][S - B[i]]:
            ans += "B"
            S -= B[i]

print(ans[::-1])
