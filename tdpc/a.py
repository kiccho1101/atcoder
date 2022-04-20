N = int(input())
ps = list(map(int, input().split()))


# dp[i]: 和がiになるかどうか
dp = [False] * 10001

dp[0] = True
for i in range(N):
    for j in reversed(range(len(dp))):
        if dp[j]:
            dp[j + ps[i]] = True

print(sum(dp))
