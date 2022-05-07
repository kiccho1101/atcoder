N = int(input())

ab = [list(map(int, input().split())) for _ in range(N)]

secs = [a / b for a, b in ab]
middle = sum(secs) / 2

ans = 0
curr = 0
for i, (a, b) in enumerate(ab):
    diff = middle - (curr + secs[i])
    if diff > 0:
        curr += secs[i]
        ans += a
    else:
        ans += (middle - curr) * b
        break

print(ans)
