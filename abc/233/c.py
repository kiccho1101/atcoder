from functools import reduce
from itertools import product

N, X = map(int, input().split())

A = [list(map(int, input().split()))[1:] for _ in range(N)]


ans = 0
for xs in product(*A):
    mul = reduce((lambda x, y: x * y), xs)
    if mul == X:
        ans += 1
print(ans)
