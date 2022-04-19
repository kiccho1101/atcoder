N, M = map(int, input().split())

reqs = [tuple(map(int, input().split())) for _ in range(M)]

ans = 0
curr = -1
reqs.sort(key=lambda x: x[1])
for a, b in reqs:
    if a >= curr:
        ans += 1
        curr = b

print(ans)
