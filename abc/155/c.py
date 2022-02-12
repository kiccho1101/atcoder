from collections import defaultdict


counter = defaultdict(int)
n = int(input())
votes = [input() for _ in range(n)]

for v in votes:
    counter[v] += 1

result = [(v, k) for k, v in counter.items()]
result.sort(reverse=True)

max_v = result[0][0]
max_votes = []
for v, r in result:
    if v != max_v:
        break
    max_votes.append(r)

max_votes.sort()
for v in max_votes:
    print(v)
