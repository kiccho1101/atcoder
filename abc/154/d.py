N, K = map(int, input().split())
ps = list(map(int, input().split()))


def get_sum(n):
    return ((n + 1) * n) // 2


es = []
for i in range(N):
    es.append(get_sum(ps[i]) / ps[i])


for i in range(1, N):
    es[i] = es[i - 1] + es[i]


ans = -1
for i in range(N):
    if i + K - 1 >= N:
        break
    e = es[i + K - 1]
    if i - 1 >= 0:
        e -= es[i - 1]
    ans = max(ans, e)

print(ans)
