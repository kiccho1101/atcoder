# %%
import math

T = int(input())

L, X, Y = map(int, input().split())

Q = int(input())

ts = [int(input()) for _ in range(Q)]

for t in ts:
    y = -L / 2 * math.sin((2 * math.pi) / T * t)
    z = L / 2 * (1 - math.cos((2 * math.pi) / T * t))
    d = math.sqrt(X ** 2 + (Y - y) ** 2 + z ** 2)
    dz = abs(z)
    ans = math.degrees(math.asin(dz / d))
    print(ans)
