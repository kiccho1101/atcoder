import collections


N = int(input())
A = list(map(int, input().split()))

counter = collections.Counter()
for a in A:
    counter[a - 1] += 1
    counter[a] += 1
    counter[a + 1] += 1

print(counter.most_common(1)[0][1])
