from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

A_cum = [0] * (N + 1)

for i in range(N):
    A_cum[i + 1] = A_cum[i] + A[i]


counter = defaultdict(int)
ans = 0
for i in range(1, N + 1):
    counter[A_cum[i - 1]] += 1
    ans += counter[A_cum[i] - K]

print(ans)
