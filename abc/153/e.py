import mailbox


INF = 10 ** 18
H, N = map(int, input().split())
magics = [tuple(map(int, input().split())) for _ in range(N)]
dp = [INF] * (H + 1)

dp[0] = 0
for h in range(H + 1):
    for a, b in magics:
        next_h = min(h + a, H)
        dp[next_h] = min(dp[next_h], dp[h] + b)

print(dp[-1])
