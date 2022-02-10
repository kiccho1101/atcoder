N = int(input())

a = []
b = []
for _ in range(N):
    a.append(list(map(int, input().split())))
for _ in range(N):
    b.append(list(map(int, input().split())))

b.sort()
used = [False] * N
ans = 0
for bx, by in b:
    max_ay = -1
    max_ai = -1
    for ai, [ax, ay] in enumerate(a):
        if ax < bx and ay < by and max_ay < ay and not used[ai]:
            max_ay = ay
            max_ai = ai
    if max_ai != -1:
        ans += 1
        used[max_ai] = True

print(ans)
