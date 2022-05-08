import collections


def nC2(n):
    if n == 1:
        return 0
    return n * (n - 1) // 2


N = int(input())
A = list(map(int, input().split()))

cnt = collections.defaultdict(int)
for a in A:
    cnt[a] += 1

total = 0
for c in cnt.values():
    if c >= 2:
        total += nC2(c)

for a in A:
    c = cnt[a]
    if c <= 1:
        print(total)
    else:
        diff = nC2(c) - nC2(c - 1)
        print(total - diff)
