import math


N, H = map(int, input().split())

a = []
b = []
for _ in range(N):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

ans = 0
a_max = max(a)
b.sort()
while H > 0 and b:
    b_max = b.pop()
    if b_max > a_max:
        H -= b_max
        ans += 1
    else:
        break

if H <= 0:
    print(ans)
else:
    print(ans + math.ceil(H / a_max))
