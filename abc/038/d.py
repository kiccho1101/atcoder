import bisect


N = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(N)]
boxes.sort(key=lambda x: (x[0], -x[1]))

INF = 10 ** 18
dp = [INF] * N

for w, h in boxes:
    dp[bisect.bisect_left(dp, h)] = h

print(bisect.bisect_left(dp, INF))
