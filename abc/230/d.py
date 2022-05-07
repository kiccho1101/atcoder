N, D = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(N)]

lr.sort(key=lambda item: item[1])

ans = 0
curr = -(10 ** 18)
for left, right in lr:
    if curr + D <= left:
        curr = right
        ans += 1

print(ans)
