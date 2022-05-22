import itertools


N, K = map(int, input().split())
Ts = [list(map(int, input().split())) for _ in range(N)]

ans = "Nothing"
for a in itertools.product(range(K), repeat=N):
    s = Ts[0][a[0]]
    for i, idx in enumerate(list(a[1:])):
        s ^= Ts[i + 1][idx]
    if s == 0:
        ans = "Found"

print(ans)
