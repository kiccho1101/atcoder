N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i][j]: i番目までの数列で、(A,A),(A,B),(B,A),(B,B)で条件を満たすかどうか
dp = [[False] * 4 for _ in range(N + 1)]

for j in range(4):
    dp[0][j] = True

for i in range(N - 1):
    # (A,A)
    dp[i + 1][0] |= dp[i][0] and abs(A[i + 1] - A[i]) <= K
    dp[i + 1][0] |= dp[i][2] and abs(A[i + 1] - A[i]) <= K

    # (A,B)
    dp[i + 1][1] |= dp[i][0] and abs(B[i + 1] - A[i]) <= K
    dp[i + 1][1] |= dp[i][2] and abs(B[i + 1] - A[i]) <= K

    # (B,A)
    dp[i + 1][2] |= dp[i][1] and abs(A[i + 1] - B[i]) <= K
    dp[i + 1][2] |= dp[i][3] and abs(A[i + 1] - B[i]) <= K

    # (B,B)
    dp[i + 1][3] |= dp[i][1] and abs(B[i + 1] - B[i]) <= K
    dp[i + 1][3] |= dp[i][3] and abs(B[i + 1] - B[i]) <= K


ans = False
for j in range(4):
    ans |= dp[N - 1][j]

if ans:
    print("Yes")
else:
    print("No")
