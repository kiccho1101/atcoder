N = int(input())

ps = []
for _ in range(N):
    x, l = map(int, input().split())
    ps.append((x - l, x + l))

ps.sort(key=lambda item: item[1])

curr = -float("inf")

ans = 0
for first, second in ps:
    if first >= curr:
        ans += 1
        curr = second

print(ans)
