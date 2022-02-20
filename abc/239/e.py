import sys

sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())
X = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

qs = [list(map(int, input().split())) for _ in range(Q)]

db = {}


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] >= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged[:20]


def dfs(x, past=-1):
    if x == past:
        return
    for to in graph[x]:
        if to == past:
            continue
        dfs(to, x)

        d = [X[to]]
        for j in graph[to]:
            if j in db:
                d = merge(d, db[j])
        db[to] = d


dfs(0)

d = [X[0]]
for j in graph[0]:
    d = merge(d, db[j])
db[0] = d


for v, k in qs:
    print(db[v - 1][k - 1])
