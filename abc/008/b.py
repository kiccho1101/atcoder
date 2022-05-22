import collections


N = int(input())
S = [input() for _ in range(N)]

counter = collections.Counter()
for s in S:
    counter[s] += 1

print(counter.most_common(1)[0][0])
