import bisect

N = int(input())
cs = [int(input()) for _ in range(N)]

INF = 10 ** 18
dp = [INF] * N

for c in cs:
    j = bisect.bisect_left(dp, c)
    dp[j] = c

print(N - bisect.bisect_left(dp, INF))
