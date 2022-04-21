from collections import defaultdict


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N, D = map(int, input().split())
dp = defaultdict(int)
ndp = defaultdict(int)
dp[D] = 1

for i in range(N):
    print(i, dp)
    ndp = defaultdict(int)
    for k, v in dp.items():
        for j in range(1, 7):
            g = gcd(k, j)
            if g != 1:
                ndp[k // g] += v
            else:
                ndp[k] += v
    dp = ndp

ans = ndp[1] / pow(6, N)
print(ans)
