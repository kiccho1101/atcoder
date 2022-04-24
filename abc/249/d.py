from collections import defaultdict
import math


N = int(input())
A = list(map(int, input().split()))

db = defaultdict(int)
for a in A:
    db[a] += 1


def get_divisor(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
    return ret


ans = 0
for a in A:
    divisors = get_divisor(a)
    for d1 in divisors:
        d2 = a // d1
        if d1 != d2:
            ans += 2 * db[d1] * db[d2]
        else:
            ans += db[d1] * db[d1]
print(ans)
