import bisect


def sieve_eratosthenes(n):
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, int(n ** 0.5) + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return [2] + [p for p in range(3, n + 1, 2) if primes[p]]


ans = 0
N = int(input())
primes = sieve_eratosthenes(10 ** 6)
for i, p in enumerate(primes):
    if i == 0:
        continue
    target = N / pow(p, 3)
    idx = bisect.bisect_right(primes, target)
    if idx != 0:
        ans += min(i, idx)

print(ans)
