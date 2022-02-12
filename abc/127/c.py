N, M = map(int, input().split())

cum = [0] * (N + 2)

for _ in range(M):
    l, r = map(int, input().split())
    cum[l] += 1
    cum[r + 1] -= 1

for i in range(N):
    cum[i + 1] += cum[i]

ans = 0
for c in cum:
    if c == M:
        ans += 1

print(ans)
