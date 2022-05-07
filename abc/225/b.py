import collections


N = int(input())

edges = collections.defaultdict(set)
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

flag = False
for to in edges.values():
    if len(to) == N - 1:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
