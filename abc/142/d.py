import sys
from collections import defaultdict

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def primes(n):
    ps = defaultdict(int)
    while n % 2 == 0:
        ps[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            ps[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        ps[n] += 1
    return ps


A, B = map(int, input().split())
g = gcd(A, B)
print(len(primes(g).keys()) + 1)
