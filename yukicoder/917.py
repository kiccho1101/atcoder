from collections import defaultdict


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


N = int(input())
A = list(map(int, input().split()))


# dp[i][j]: i番目まででgcdがjになる場合の数
dp = [defaultdict(int) for _ in range(N + 1)]


for i in range(N):
    dp[i][A[i]] += 1
    for j in range(i + 1, N):
        for k in dp[i].keys():
            dp[j][gcd(k, A[j])] += dp[i][k]

ans = 0
for i in range(N):
    ans += dp[i][1]
print(ans)
