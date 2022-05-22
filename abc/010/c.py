import math


txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

ans = "NO"
for x, y in xy:
    dist = math.sqrt((x - txa) ** 2 + (y - tya) ** 2) + math.sqrt(
        (x - txb) ** 2 + (y - tyb) ** 2
    )
    if dist / V <= T:
        ans = "YES"

print(ans)
