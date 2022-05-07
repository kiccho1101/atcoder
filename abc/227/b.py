N = int(input())
ss = list(map(int, input().split()))

possible = [False] * 1001

for a in range(1, 1001):
    for b in range(1, 1001):
        s = 4 * a * b + 3 * a + 3 * b
        if s <= 1000:
            possible[s] = True

ans = 0
for s in ss:
    if not possible[s]:
        ans += 1

print(ans)
