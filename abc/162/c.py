import itertools
import math


def gcd(a, b, c):
    gcd_2 = math.gcd(a, b)
    return math.gcd(gcd_2, c)


K = int(input())
ans = 0

for i in range(1, K + 1):
    ans += i

for i, j in itertools.combinations(range(1, K + 1), 2):
    ans += 6 * math.gcd(i, j)

for i, j, k in itertools.combinations(range(1, K + 1), 3):
    ans += 6 * gcd(i, j, k)

print(ans)
