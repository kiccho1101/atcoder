from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    A[i] += A[i - 1]

counter = defaultdict(int)
for i in range(N):
    counter[A[i]] += 1

counter[0] += 1
ans = 0
for cnt in counter.values():
    ans += cnt * (cnt - 1) // 2

print(ans)
