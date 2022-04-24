def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            j = i + i
            while j <= n:
                is_prime[j] = False
                j += i
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


n = int(input())
primes = get_primes(n)

N = len(primes)

# dp[i][j]: i番目までの素数で和がjになる和の回数の最大値
dp = [[-1] * (n + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
    for j in range(n + 1):
        if dp[i][j] != -1:
            dp[i + 1][j] = dp[i][j]
        if j - primes[i] >= 0 and dp[i][j - primes[i]] != -1:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - primes[i]] + 1)

print(dp[N][n])
