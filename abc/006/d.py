import bisect


N = int(input())
A = [int(input()) for _ in range(N)]

INF = 10 ** 18
dp = [INF] * N
for i in range(N):
    dp[bisect.bisect_left(dp, A[i])] = A[i]

lis = bisect.bisect_left(dp, INF)
print(N - lis)
