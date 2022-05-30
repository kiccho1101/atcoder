from math import gcd


N, A, B = map(int, input().split())

AB = gcd(A, B)

a = N // A
b = N // B
ab = N // AB


def s(r, n):
    return n * (2 * r + (n - 1) * r) // 2


ans = s(1, N) // 2 - s(A, a) - s(B, b) + s(AB, ab)

print(ans)
