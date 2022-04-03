import functools


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N, K = map(int, input().split())
A = list(map(int, input().split()))

G = functools.reduce(gcd, A)

if K % G == 0 and max(A) >= K:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
