import collections


N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = collections.Counter()

for a in A:
    counter[a] += 1

mc = counter.most_common()

ans = 0
if len(mc) > K:
    for i in range(K, len(mc)):
        ans += mc[i][1]

print(ans)
